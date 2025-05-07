import streamlit as st
import requests
import json
import uuid
import os
import traceback

# Configuration
AGENT_BASE_URL = "https://omnipresense-ai.onrender.com/"  # ADK local server
AGENTS_DIR = "agents"  # Define the agents directory

def get_available_agents(base_path=AGENTS_DIR):
    """Scans the AGENTS_DIR for directories that are considered agents."""
    agents = []
    if not os.path.isdir(base_path):
        # If AGENTS_DIR doesn't exist, log it or handle as needed, but return empty list.
        # For Streamlit, we can let the UI handle the "no agents found" message.
        return []

    try:
        # Scan the specified base_path for directories
        for entry in os.scandir(base_path):
            if entry.is_dir():
                # Exclude common non-agent directories like .git, .venv, __pycache__
                if not entry.name.startswith('.') and entry.name != "__pycache__":
                    agents.append(entry.name)
    except FileNotFoundError:
        # This case should ideally be caught by the os.path.isdir check earlier,
        # but as a safeguard:
        return []
    except Exception as e:
        # Log this error for debugging if it occurs
        # print(f"Error scanning for agents: {e}")
        return [] # Return empty list on other errors to prevent app crash
    return agents

def create_agent_session(user_id: str, session_id: str, agent_name: str):
    """Creates a new session with the specified agent."""
    url = f"{AGENT_BASE_URL}/apps/{agent_name}/users/{user_id}/sessions/{session_id}"
    headers = {"Content-Type": "application/json"}
    data = {"state": {}}
    response = None
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error creating session with {agent_name}: {e}")
        if response is not None:
            st.error(f"Response content: {response.content.decode() if response.content else 'No response content'}")
        else:
            st.error("No response object from server.")
        return None

def send_query_to_agent(user_id: str, session_id: str, query: str, agent_name: str):
    """Sends a query to the specified agent and gets the response, showing status."""
    url = f"{AGENT_BASE_URL}/run"
    headers = {"Content-Type": "application/json"}
    payload = {
        "app_name": agent_name,
        "user_id": user_id,
        "session_id": session_id,
        "new_message": {
            "role": "user",
            "parts": [{"text": query}]
        }
    }
    response_obj = None
    agent_final_text_response = ""

    with st.status(f"Querying {agent_name}...", expanded=True) as status_container:
        try:
            status_container.write(f"Sending request to {agent_name}...")
            response_obj = requests.post(url, headers=headers, json=payload)
            response_obj.raise_for_status()

            status_container.write(f"Received response, processing events...")
            events = response_obj.json()

            tool_called_flag = False

            for event_idx, event in enumerate(events):
                content = event.get("content", {})
                role = content.get("role")
                parts = content.get("parts", [])

                if not parts:
                    continue

                for part in parts:
                    if "function_call" in part:
                        tool_called_flag = True
                        fc = part["function_call"]
                        tool_name = fc.get("name", "Unknown tool")
                        args_str = json.dumps(fc.get("args", {}))
                        status_container.write(f"⏳ Agent wants to call tool: `{tool_name}` with args: `{args_str}`")

                    elif "function_response" in part:
                        tool_called_flag = True # A response implies a call was made
                        fr = part["function_response"]
                        tool_name = fr.get("name", "Unknown tool")
                        is_error = False
                        response_data = fr.get("response")
                        if isinstance(response_data, dict) and response_data.get("status") == "error":
                            is_error = True
                            error_details = response_data.get("error", {}).get("message", "Tool execution error")
                            status_container.write(f"❌ Tool `{tool_name}` execution failed: {error_details}")
                        else:
                            status_container.write(f"✅ Tool `{tool_name}` executed.")

                    elif "text" in part and part["text"] and role == "model":
                        current_text = part["text"].strip()
                        if current_text:
                            agent_final_text_response += current_text + " "
                            status_container.write(f"🤖 Agent says: \"{current_text}\"")

            final_response_to_display = agent_final_text_response.strip()

            if not final_response_to_display:
                if tool_called_flag:
                    final_response_to_display = f"{agent_name} processed the request (tools were called) but returned no final text message."
                else:
                    final_response_to_display = f"{agent_name} processed the request but returned no specific text response."
                status_container.update(label=f"Processing complete for {agent_name}.", state="complete", expanded=False)
            else:
                status_container.update(label=f"{agent_name} finished.", state="complete", expanded=False)

            return final_response_to_display

        except requests.exceptions.HTTPError as e:
            error_message = f"HTTP error with {agent_name}: {e}"
            if response_obj and response_obj.text:
                error_message += f" | Response: {response_obj.text[:300]}..."
            st.error(error_message)
            if 'status_container' in locals():
                status_container.update(label=f"HTTP Error with {agent_name}!", state="error", expanded=True)
                status_container.write(f"Details: {error_message}")
            return f"Error: HTTP issue while communicating with {agent_name}."

        except requests.exceptions.RequestException as e:
            error_message = f"Network error contacting {agent_name}: {e}"
            st.error(error_message)
            if 'status_container' in locals():
                status_container.update(label=f"Network Error with {agent_name}!", state="error", expanded=True)
                status_container.write(f"Details: {error_message}")
            return f"Error: Could not connect to agent {agent_name}."

        except json.JSONDecodeError:
            error_message = f"Error decoding JSON response from {agent_name}."
            if response_obj and response_obj.text:
                 error_message += f" | Response Text: {response_obj.text[:300]}..."
            st.error(error_message)
            if 'status_container' in locals():
                status_container.update(label=f"Response Format Error from {agent_name}!", state="error", expanded=True)
                status_container.write(f"Details: {error_message}")
            return f"Error: Invalid response format from agent {agent_name}."

        except Exception as e:
            error_message = f"An unexpected error occurred while processing {agent_name}'s response: {str(e)}"
            tb_str = traceback.format_exc()
            st.error(error_message)
            if 'status_container' in locals():
                status_container.update(label=f"Unexpected Error with {agent_name}!", state="error", expanded=True)
                status_container.write(f"Details: {error_message}\\nTraceback: {tb_str}")
            return f"Error: An unexpected issue occurred with {agent_name}."

st.title("OmniPresense AI")

# Initialize session state variables if they don't exist
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())
if "messages" not in st.session_state:
    st.session_state.messages = []
if "session_created" not in st.session_state:
    st.session_state.session_created = False

if "available_agents" not in st.session_state: # Get agents once per session
    st.session_state.available_agents = get_available_agents()

if "selected_agent" not in st.session_state: # Initialize selected_agent
    st.session_state.selected_agent = st.session_state.available_agents[0] if st.session_state.available_agents else None

# Store the previously selected agent to detect changes
if "previous_selected_agent" not in st.session_state:
    st.session_state.previous_selected_agent = None


# --- Sidebar ---
st.sidebar.title("Agent Configuration")

if not st.session_state.available_agents:
    st.sidebar.error(f"No agents found in the '{AGENTS_DIR}' directory. Please add agent folders there.")
    st.info(f"Instructions: Create a directory named '{AGENTS_DIR}' in your project root, and place each agent in its own sub-directory within '{AGENTS_DIR}'.")
    # Prevent the rest of the app from trying to run if no agents are available
    st.stop()

# Agent selection dropdown
# Determine the index for the selectbox. If selected_agent is not in available_agents (e.g. after deleting an agent folder)
# default to the first available agent or 0 if the list is somehow empty (though st.stop() should prevent that).
current_selection_index = 0
if st.session_state.selected_agent and st.session_state.selected_agent in st.session_state.available_agents:
    current_selection_index = st.session_state.available_agents.index(st.session_state.selected_agent)
elif st.session_state.available_agents: # If current selection is invalid, but agents are available, select first
    st.session_state.selected_agent = st.session_state.available_agents[0]
    # No need to set current_selection_index to 0 here as it defaults to 0
else: # Should not be reached due to st.stop() if available_agents is empty
    st.session_state.selected_agent = None


newly_selected_agent = st.sidebar.selectbox(
    "Choose an Agent:",
    options=st.session_state.available_agents,
    index=current_selection_index, # Use the safe index
    key="agent_selector" # Add a key for stability
)

# Detect agent change and reset session
if newly_selected_agent != st.session_state.selected_agent:
    st.session_state.selected_agent = newly_selected_agent
    st.session_state.messages = []
    st.session_state.session_id = str(uuid.uuid4())
    st.session_state.session_created = False
    st.sidebar.info(f"Switched to agent: {st.session_state.selected_agent}. New session will start.")
    st.session_state.previous_selected_agent = st.session_state.selected_agent # Update previous before potential rerun
    st.rerun() # Rerun to apply changes, clear main page and re-trigger session creation

st.session_state.previous_selected_agent = st.session_state.selected_agent

# --- Main Page ---

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Attempt to create a session if an agent is selected and session not already created
if st.session_state.selected_agent and not st.session_state.session_created:
    with st.spinner(f"Connecting to agent: {st.session_state.selected_agent}..."):
        session_info = create_agent_session(st.session_state.user_id, st.session_state.session_id, st.session_state.selected_agent)
        if session_info:
            st.session_state.session_created = True
            if not st.session_state.messages:
                st.success(f"Connected to agent: {st.session_state.selected_agent}!")
                greeting_message = (
                    f"Hello! I am {st.session_state.selected_agent}, your AI scheduling assistant. "
                    "I can help you book meetings and find available time slots.\n\n"
                    "**To book a meeting, you can say something like:**\n"
                    "*   'Book a meeting for John Doe at john.doe@example.com tomorrow at 10am.'\n"
                    "*   'Schedule a 30-minute meeting with Jane Smith (jane@example.com) next Tuesday at 2 PM.'\n\n"
                    "**To find available slots, you can ask:**\n"
                    "*   'Are there any open slots tomorrow afternoon?'\n"
                    "*   'Find available times next week between 9am and 5pm.'\n\n"
                    "How can I assist you today?"
                )
                st.session_state.messages.append({"role": "assistant", "content": greeting_message})
                st.rerun() # Rerun to display the greeting message
        else:
            st.error(f"Failed to connect to agent: {st.session_state.selected_agent}. Ensure ADK server is running and the agent is correctly configured in the '{AGENTS_DIR}' directory.")
            st.stop()
elif not st.session_state.selected_agent: # Should be caught by sidebar logic, but as a safeguard
    st.warning("Please select an agent from the sidebar to begin.")
    st.stop()

# React to user input
if prompt := st.chat_input("What would you like to do?"):
    if not st.session_state.selected_agent:
        st.error("No agent selected. Please choose an agent from the sidebar.")
    elif not st.session_state.session_created:
        st.error("Session not created. Please wait or try re-selecting an agent.")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar=":material/person:"):
            st.markdown(prompt)

        response_text = send_query_to_agent(st.session_state.user_id, st.session_state.session_id, prompt, st.session_state.selected_agent)

        st.session_state.messages.append({"role": "assistant", "content": response_text})
        with st.chat_message("assistant"):
            st.markdown(response_text)
