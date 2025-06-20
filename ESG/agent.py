from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from Tools.file_search import file_search
from google.adk.tools import agent_tool

# Industry Finder Agent
industry_finder_agent = Agent(
    name="Industry_Finder_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini", temperature=0.1, max_tokens=200),
    description="An agent that helps identify and classify industries based on business descriptions",
    instruction= open("Prompts/industry_finder.md").read(),
    tools=[file_search]
)

# All SASB Industry Standards Agents
apparel_accessories_footwear_agent = Agent(
    name="Apparel_Accessories_and_Footwear_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Apparel, Accessories & Footwear industry",
    instruction= open("Prompts/apparel_accessories_footwear.md").read(),
    tools=[file_search]
)
appliance_manufacturing_agent = Agent(
    name="Appliance_Manufacturing_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Appliance Manufacturing industry",
    instruction= open("Prompts/appliance_manufacturing.md").read(),
    tools=[file_search]
)
building_products_furnishings_agent = Agent(
    name="Building_Products_and_Furnishings_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Building Products & Furnishings industry",
    instruction= open("Prompts/building_products_furnishings.md").read(),
    tools=[file_search]
)
e_commerce_agent = Agent(
    name="ECommerce_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the E-Commerce industry",
    instruction= open("Prompts/e_commerce.md").read(),
    tools=[file_search]
)
household_personal_products_agent = Agent(
    name="Household_and_Personal_Products_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Household & Personal Products industry",
    instruction= open("Prompts/household_personal_products.md").read(),
    tools=[file_search]
)
multi_retail_dist_agent = Agent(
    name="Multiline_Retailers_Distributors_Standards", # Shortened from "Multiline_and_Specialty_Retailers_and_Distributors_Standards_Agent"
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Multiline and Specialty Retailers & Distributors industry",
    instruction= open("Prompts/multiline_specialty_retailers_distributors.md").read(),
    tools=[file_search]
)
toys_sporting_goods_agent = Agent(
    name="Toys_and_Sporting_Goods_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Toys & Sporting Goods industry",
    instruction= open("Prompts/toys_sporting_goods.md").read(),
    tools=[file_search]
)
coal_operations_agent = Agent(
    name="Coal_Operations_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Coal Operations industry",
    instruction= open("Prompts/coal_operations.md").read(),
    tools=[file_search]
)
construction_materials_agent = Agent(
    name="Construction_Materials_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Construction Materials industry",
    instruction= open("Prompts/construction_materials.md").read(),
    tools=[file_search]
)
iron_steel_producers_agent = Agent(
    name="Iron_and_Steel_Producers_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Iron & Steel Producers industry",
    instruction= open("Prompts/iron_steel_producers.md").read(),
    tools=[file_search]
)
metals_mining_agent = Agent(
    name="Metals_and_Mining_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Metals & Mining industry",
    instruction= open("Prompts/metals_mining.md").read(),
    tools=[file_search]
)
oil_gas_exploration_production_agent = Agent(
    name="Oil_and_Gas_Exploration_and_Production_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Oil & Gas – Exploration & Production industry",
    instruction= open("Prompts/oil_gas_exploration_production.md").read(),
    tools=[file_search]
)
oil_gas_midstream_agent = Agent(
    name="Oil_and_Gas_Midstream_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Oil & Gas – Midstream industry",
    instruction= open("Prompts/oil_gas_midstream.md").read(),
    tools=[file_search]
)
oil_gas_refining_marketing_agent = Agent(
    name="Oil_and_Gas_Refining_and_Marketing_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Oil & Gas – Refining & Marketing industry",
    instruction= open("Prompts/oil_gas_refining_marketing.md").read(),
    tools=[file_search]
)
oil_gas_services_agent = Agent(
    name="Oil_and_Gas_Services_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Oil & Gas – Services industry",
    instruction= open("Prompts/oil_gas_services.md").read(),
    tools=[file_search]
)
asset_management_custody_activities_agent = Agent(
    name="Asset_Management_and_Custody_Activities_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Asset Management & Custody Activities industry",
    instruction= open("Prompts/asset_management_custody_activities.md").read(),
    tools=[file_search]
)
commercial_banks_agent = Agent(
    name="Commercial_Banks_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Commercial Banks industry",
    instruction= open("Prompts/commercial_banks.md").read(),
    tools=[file_search]
)
consumer_finance_agent = Agent(
    name="Consumer_Finance_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Consumer Finance industry",
    instruction= open("Prompts/consumer_finance.md").read(),
    tools=[file_search]
)
insurance_agent = Agent(
    name="Insurance_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Insurance industry",
    instruction= open("Prompts/insurance.md").read(),
    tools=[file_search]
)
investment_banking_brokerage_agent = Agent(
    name="Investment_Banking_and_Brokerage_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Investment Banking & Brokerage industry",
    instruction= open("Prompts/investment_banking_brokerage.md").read(),
    tools=[file_search]
)
mortgage_finance_agent = Agent(
    name="Mortgage_Finance_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Mortgage Finance industry",
    instruction= open("Prompts/mortgage_finance.md").read(),
    tools=[file_search]
)
security_commodity_exchanges_agent = Agent(
    name="Security_and_Commodity_Exchanges_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Security & Commodity Exchanges industry",
    instruction= open("Prompts/security_commodity_exchanges.md").read(),
    tools=[file_search]
)
agricultural_products_agent = Agent(
    name="Agricultural_Products_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Agricultural Products industry",
    instruction= open("Prompts/agricultural_products.md").read(),
    tools=[file_search]
)
alcoholic_beverages_agent = Agent(
    name="Alcoholic_Beverages_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Alcoholic Beverages industry",
    instruction= open("Prompts/alcoholic_beverages.md").read(),
    tools=[file_search]
)
food_retailers_distributors_agent = Agent(
    name="Food_Retailers_and_Distributors_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Food Retailers & Distributors industry",
    instruction= open("Prompts/food_retailers_distributors.md").read(),
    tools=[file_search]
)
meat_poultry_dairy_agent = Agent(
    name="Meat_Poultry_and_Dairy_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Meat, Poultry & Dairy industry",
    instruction= open("Prompts/meat_poultry_dairy.md").read(),
    tools=[file_search]
)
non_alcoholic_beverages_agent = Agent(
    name="Non_Alcoholic_Beverages_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Non-Alcoholic Beverages industry",
    instruction= open("Prompts/non_alcoholic_beverages.md").read(),
    tools=[file_search]
)
processed_foods_agent = Agent(
    name="Processed_Foods_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Processed Foods industry",
    instruction= open("Prompts/processed_foods.md").read(),
    tools=[file_search]
)
restaurants_agent = Agent(
    name="Restaurants_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Restaurants industry",
    instruction= open("Prompts/restaurants.md").read(),
    tools=[file_search]
)
tobacco_agent = Agent(
    name="Tobacco_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Tobacco industry",
    instruction= open("Prompts/tobacco.md").read(),
    tools=[file_search]
)
biotechnology_pharmaceuticals_agent = Agent(
    name="Biotechnology_and_Pharmaceuticals_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Biotechnology & Pharmaceuticals industry",
    instruction= open("Prompts/biotechnology_pharmaceuticals.md").read(),
    tools=[file_search]
)
drug_retailers_agent = Agent(
    name="Drug_Retailers_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Drug Retailers industry",
    instruction= open("Prompts/drug_retailers.md").read(),
    tools=[file_search]
)
health_care_delivery_agent = Agent(
    name="Health_Care_Delivery_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Health Care Delivery industry",
    instruction= open("Prompts/health_care_delivery.md").read(),
    tools=[file_search]
)
health_care_distributors_agent = Agent(
    name="Health_Care_Distributors_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Health Care Distributors industry",
    instruction= open("Prompts/health_care_distributors.md").read(),
    tools=[file_search]
)
managed_care_agent = Agent(
    name="Managed_Care_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Managed Care industry",
    instruction= open("Prompts/managed_care.md").read(),
    tools=[file_search]
)
medical_equipment_supplies_agent = Agent(
    name="Medical_Equipment_and_Supplies_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Medical Equipment & Supplies industry",
    instruction= open("Prompts/medical_equipment_supplies.md").read(),
    tools=[file_search]
)
electric_utilities_power_generators_agent = Agent(
    name="Electric_Utilities_and_Power_Generators_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Electric Utilities & Power Generators industry",
    instruction= open("Prompts/electric_utilities_power_generators.md").read(),
    tools=[file_search]
)
engineering_construction_services_agent = Agent(
    name="Engineering_and_Construction_Services_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Engineering & Construction Services industry",
    instruction= open("Prompts/engineering_construction_services.md").read(),
    tools=[file_search]
)
gas_utilities_distributors_agent = Agent(
    name="Gas_Utilities_and_Distributors_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Gas Utilities & Distributors industry",
    instruction= open("Prompts/gas_utilities_distributors.md").read(),
    tools=[file_search]
)
home_builders_agent = Agent(
    name="Home_Builders_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Home Builders industry",
    instruction= open("Prompts/home_builders.md").read(),
    tools=[file_search]
)
real_estate_agent = Agent(
    name="Real_Estate_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Real Estate industry",
    instruction= open("Prompts/real_estate.md").read(),
    tools=[file_search]
)
real_estate_services_agent = Agent(
    name="Real_Estate_Services_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Real Estate Services industry",
    instruction= open("Prompts/real_estate_services.md").read(),
    tools=[file_search]
)
waste_management_agent = Agent(
    name="Waste_Management_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Waste Management industry",
    instruction= open("Prompts/waste_management.md").read(),
    tools=[file_search]
)
water_utilities_services_agent = Agent(
    name="Water_Utilities_and_Services_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Water Utilities & Services industry",
    instruction= open("Prompts/water_utilities_services.md").read(),
    tools=[file_search]
)
biofuels_agent = Agent(
    name="Biofuels_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Biofuels industry",
    instruction= open("Prompts/biofuels.md").read(),
    tools=[file_search]
)
forestry_management_agent = Agent(
    name="Forestry_Management_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Forestry Management industry",
    instruction= open("Prompts/forestry_management.md").read(),
    tools=[file_search]
)
fuel_cells_industrial_batteries_agent = Agent(
    name="Fuel_Cells_and_Industrial_Batteries_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Fuel Cells & Industrial Batteries industry",
    instruction= open("Prompts/fuel_cells_industrial_batteries.md").read(),
    tools=[file_search]
)
pulp_paper_products_agent = Agent(
    name="Pulp_and_Paper_Products_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Pulp & Paper Products industry",
    instruction= open("Prompts/pulp_paper_products.md").read(),
    tools=[file_search]
)
solar_technology_project_developers_agent = Agent(
    name="Solar_Technology_and_Project_Developers_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Solar Technology & Project Developers industry",
    instruction= open("Prompts/solar_technology_project_developers.md").read(),
    tools=[file_search]
)
wind_technology_project_developers_agent = Agent(
    name="Wind_Technology_and_Project_Developers_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Wind Technology & Project Developers industry",
    instruction= open("Prompts/wind_technology_project_developers.md").read(),
    tools=[file_search]
)
aerospace_defence_agent = Agent(
    name="Aerospace_and_Defence_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Aerospace & Defence industry",
    instruction= open("Prompts/aerospace_defence.md").read(),
    tools=[file_search]
)
chemicals_agent = Agent(
    name="Chemicals_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Chemicals industry",
    instruction= open("Prompts/chemicals.md").read(),
    tools=[file_search]
)
containers_packaging_agent = Agent(
    name="Containers_and_Packaging_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Containers & Packaging industry",
    instruction= open("Prompts/containers_packaging.md").read(),
    tools=[file_search]
)
electrical_electronic_equipment_agent = Agent(
    name="Electrical_and_Electronic_Equipment_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Electrical & Electronic Equipment industry",
    instruction= open("Prompts/electrical_electronic_equipment.md").read(),
    tools=[file_search]
)
industrial_machinery_goods_agent = Agent(
    name="Industrial_Machinery_and_Goods_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Industrial Machinery & Goods industry",
    instruction= open("Prompts/industrial_machinery_goods.md").read(),
    tools=[file_search]
)
advertising_marketing_agent = Agent(
    name="Advertising_and_Marketing_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Advertising & Marketing industry",
    instruction= open("Prompts/advertising_marketing.md").read(),
    tools=[file_search]
)
casinos_gaming_agent = Agent(
    name="Casinos_and_Gaming_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Casinos & Gaming industry",
    instruction= open("Prompts/casinos_gaming.md").read(),
    tools=[file_search]
)
education_agent = Agent(
    name="Education_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Education industry",
    instruction= open("Prompts/education.md").read(),
    tools=[file_search]
)
hotels_lodging_agent = Agent(
    name="Hotels_and_Lodging_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Hotels & Lodging industry",
    instruction= open("Prompts/hotels_lodging.md").read(),
    tools=[file_search]
)
leisure_facilities_agent = Agent(
    name="Leisure_Facilities_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Leisure Facilities industry",
    instruction= open("Prompts/leisure_facilities.md").read(),
    tools=[file_search]
)
media_entertainment_agent = Agent(
    name="Media_and_Entertainment_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Media & Entertainment industry",
    instruction= open("Prompts/media_entertainment.md").read(),
    tools=[file_search]
)
professional_commercial_services_agent = Agent(
    name="Professional_and_Commercial_Services_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Professional & Commercial Services industry",
    instruction= open("Prompts/professional_commercial_services.md").read(),
    tools=[file_search]
)
elec_mfg_odm_agent = Agent(
    name="Elec_Mfg_Services_ODM_Standards", # Shortened from "Electronic_Manufacturing_Services_and_Original_Design_Manufacturing_Standards_Agent"
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Electronic Manufacturing Services & Original Design Manufacturing industry",
    instruction= open("Prompts/electronic_manufacturing_services_odm.md").read(),
    tools=[file_search]
)
hardware_agent = Agent(
    name="Hardware_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Hardware industry",
    instruction= open("Prompts/hardware.md").read(),
    tools=[file_search]
)
internet_media_services_agent = Agent(
    name="Internet_Media_and_Services_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Internet Media & Services industry",
    instruction= open("Prompts/internet_media_services.md").read(),
    tools=[file_search]
)
semiconductors_agent = Agent(
    name="Semiconductors_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Semiconductors industry",
    instruction= open("Prompts/semiconductors.md").read(),
    tools=[file_search]
)
software_it_services_agent = Agent(
    name="Software_and_IT_Services_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Software & IT Services industry",
    instruction= open("Prompts/software_it_services.md").read(),
    tools=[file_search]
)
telecommunication_services_agent = Agent(
    name="Telecommunication_Services_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Telecommunication Services industry",
    instruction= open("Prompts/telecommunication_services.md").read(),
    tools=[file_search]
)
air_freight_logistics_agent = Agent(
    name="Air_Freight_and_Logistics_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Air Freight & Logistics industry",
    instruction= open("Prompts/air_freight_logistics.md").read(),
    tools=[file_search]
)
airlines_agent = Agent(
    name="Airlines_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Airlines industry",
    instruction= open("Prompts/airlines.md").read(),
    tools=[file_search]
)
auto_parts_agent = Agent(
    name="Auto_Parts_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Auto Parts industry",
    instruction= open("Prompts/auto_parts.md").read(),
    tools=[file_search]
)
automobiles_agent = Agent(
    name="Automobiles_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Automobiles industry",
    instruction= open("Prompts/automobiles.md").read(),
    tools=[file_search]
)
car_rental_leasing_agent = Agent(
    name="Car_Rental_and_Leasing_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Car Rental & Leasing industry",
    instruction= open("Prompts/car_rental_leasing.md").read(),
    tools=[file_search]
)
cruise_lines_agent = Agent(
    name="Cruise_Lines_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Cruise Lines industry",
    instruction= open("Prompts/cruise_lines.md").read(),
    tools=[file_search]
)
marine_transportation_agent = Agent(
    name="Marine_Transportation_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Marine Transportation industry",
    instruction= open("Prompts/marine_transportation.md").read(),
    tools=[file_search]
)
rail_transportation_agent = Agent(
    name="Rail_Transportation_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Rail Transportation industry",
    instruction= open("Prompts/rail_transportation.md").read(),
    tools=[file_search]
)
road_transportation_agent = Agent(
    name="Road_Transportation_Standards_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides information about SASB standards for the Road Transportation industry",
    instruction= open("Prompts/road_transportation.md").read(),
    tools=[file_search]
)

industry_finder_agent_tool = agent_tool.AgentTool(agent=industry_finder_agent)
apparel_accessories_footwear_agent_tool = agent_tool.AgentTool(agent=apparel_accessories_footwear_agent)
appliance_manufacturing_agent_tool = agent_tool.AgentTool(agent=appliance_manufacturing_agent)
building_products_furnishings_agent_tool = agent_tool.AgentTool(agent=building_products_furnishings_agent)
e_commerce_agent_tool = agent_tool.AgentTool(agent=e_commerce_agent)
household_personal_products_agent_tool = agent_tool.AgentTool(agent=household_personal_products_agent)
multi_retail_dist_agent_tool = agent_tool.AgentTool(agent=multi_retail_dist_agent) # Renamed
toys_sporting_goods_agent_tool = agent_tool.AgentTool(agent=toys_sporting_goods_agent)
coal_operations_agent_tool = agent_tool.AgentTool(agent=coal_operations_agent)
construction_materials_agent_tool = agent_tool.AgentTool(agent=construction_materials_agent)
iron_steel_producers_agent_tool = agent_tool.AgentTool(agent=iron_steel_producers_agent)
metals_mining_agent_tool = agent_tool.AgentTool(agent=metals_mining_agent)
oil_gas_exploration_production_agent_tool = agent_tool.AgentTool(agent=oil_gas_exploration_production_agent)
oil_gas_midstream_agent_tool = agent_tool.AgentTool(agent=oil_gas_midstream_agent)
oil_gas_refining_marketing_agent_tool = agent_tool.AgentTool(agent=oil_gas_refining_marketing_agent)
oil_gas_services_agent_tool = agent_tool.AgentTool(agent=oil_gas_services_agent)
asset_management_custody_activities_agent_tool = agent_tool.AgentTool(agent=asset_management_custody_activities_agent)
commercial_banks_agent_tool = agent_tool.AgentTool(agent=commercial_banks_agent)
consumer_finance_agent_tool = agent_tool.AgentTool(agent=consumer_finance_agent)
insurance_agent_tool = agent_tool.AgentTool(agent=insurance_agent)
investment_banking_brokerage_agent_tool = agent_tool.AgentTool(agent=investment_banking_brokerage_agent)
mortgage_finance_agent_tool = agent_tool.AgentTool(agent=mortgage_finance_agent)
security_commodity_exchanges_agent_tool = agent_tool.AgentTool(agent=security_commodity_exchanges_agent)
agricultural_products_agent_tool = agent_tool.AgentTool(agent=agricultural_products_agent)
alcoholic_beverages_agent_tool = agent_tool.AgentTool(agent=alcoholic_beverages_agent)
food_retailers_distributors_agent_tool = agent_tool.AgentTool(agent=food_retailers_distributors_agent)
meat_poultry_dairy_agent_tool = agent_tool.AgentTool(agent=meat_poultry_dairy_agent)
non_alcoholic_beverages_agent_tool = agent_tool.AgentTool(agent=non_alcoholic_beverages_agent)
processed_foods_agent_tool = agent_tool.AgentTool(agent=processed_foods_agent)
restaurants_agent_tool = agent_tool.AgentTool(agent=restaurants_agent)
tobacco_agent_tool = agent_tool.AgentTool(agent=tobacco_agent)
biotechnology_pharmaceuticals_agent_tool = agent_tool.AgentTool(agent=biotechnology_pharmaceuticals_agent)
drug_retailers_agent_tool = agent_tool.AgentTool(agent=drug_retailers_agent)
health_care_delivery_agent_tool = agent_tool.AgentTool(agent=health_care_delivery_agent)
health_care_distributors_agent_tool = agent_tool.AgentTool(agent=health_care_distributors_agent)
managed_care_agent_tool = agent_tool.AgentTool(agent=managed_care_agent)
medical_equipment_supplies_agent_tool = agent_tool.AgentTool(agent=medical_equipment_supplies_agent)
electric_utilities_power_generators_agent_tool = agent_tool.AgentTool(agent=electric_utilities_power_generators_agent)
engineering_construction_services_agent_tool = agent_tool.AgentTool(agent=engineering_construction_services_agent)
gas_utilities_distributors_agent_tool = agent_tool.AgentTool(agent=gas_utilities_distributors_agent)
home_builders_agent_tool = agent_tool.AgentTool(agent=home_builders_agent)
real_estate_agent_tool = agent_tool.AgentTool(agent=real_estate_agent)
real_estate_services_agent_tool = agent_tool.AgentTool(agent=real_estate_services_agent)
waste_management_agent_tool = agent_tool.AgentTool(agent=waste_management_agent)
water_utilities_services_agent_tool = agent_tool.AgentTool(agent=water_utilities_services_agent)
biofuels_agent_tool = agent_tool.AgentTool(agent=biofuels_agent)
forestry_management_agent_tool = agent_tool.AgentTool(agent=forestry_management_agent)
fuel_cells_industrial_batteries_agent_tool = agent_tool.AgentTool(agent=fuel_cells_industrial_batteries_agent)
pulp_paper_products_agent_tool = agent_tool.AgentTool(agent=pulp_paper_products_agent)
solar_technology_project_developers_agent_tool = agent_tool.AgentTool(agent=solar_technology_project_developers_agent)
wind_technology_project_developers_agent_tool = agent_tool.AgentTool(agent=wind_technology_project_developers_agent)
aerospace_defence_agent_tool = agent_tool.AgentTool(agent=aerospace_defence_agent)
chemicals_agent_tool = agent_tool.AgentTool(agent=chemicals_agent)
containers_packaging_agent_tool = agent_tool.AgentTool(agent=containers_packaging_agent)
electrical_electronic_equipment_agent_tool = agent_tool.AgentTool(agent=electrical_electronic_equipment_agent)
industrial_machinery_goods_agent_tool = agent_tool.AgentTool(agent=industrial_machinery_goods_agent)
advertising_marketing_agent_tool = agent_tool.AgentTool(agent=advertising_marketing_agent)
casinos_gaming_agent_tool = agent_tool.AgentTool(agent=casinos_gaming_agent)
education_agent_tool = agent_tool.AgentTool(agent=education_agent)
hotels_lodging_agent_tool = agent_tool.AgentTool(agent=hotels_lodging_agent)
leisure_facilities_agent_tool = agent_tool.AgentTool(agent=leisure_facilities_agent)
media_entertainment_agent_tool = agent_tool.AgentTool(agent=media_entertainment_agent)
professional_commercial_services_agent_tool = agent_tool.AgentTool(agent=professional_commercial_services_agent)
elec_mfg_odm_agent_tool = agent_tool.AgentTool(agent=elec_mfg_odm_agent)
hardware_agent_tool = agent_tool.AgentTool(agent=hardware_agent)
internet_media_services_agent_tool = agent_tool.AgentTool(agent=internet_media_services_agent)
semiconductors_agent_tool = agent_tool.AgentTool(agent=semiconductors_agent)
software_it_services_agent_tool = agent_tool.AgentTool(agent=software_it_services_agent)
telecommunication_services_agent_tool = agent_tool.AgentTool(agent=telecommunication_services_agent)
air_freight_logistics_agent_tool = agent_tool.AgentTool(agent=air_freight_logistics_agent)
airlines_agent_tool = agent_tool.AgentTool(agent=airlines_agent)
auto_parts_agent_tool = agent_tool.AgentTool(agent=auto_parts_agent)
automobiles_agent_tool = agent_tool.AgentTool(agent=automobiles_agent)
car_rental_leasing_agent_tool = agent_tool.AgentTool(agent=car_rental_leasing_agent)
cruise_lines_agent_tool = agent_tool.AgentTool(agent=cruise_lines_agent)
marine_transportation_agent_tool = agent_tool.AgentTool(agent=marine_transportation_agent)
rail_transportation_agent_tool = agent_tool.AgentTool(agent=rail_transportation_agent)
road_transportation_agent_tool = agent_tool.AgentTool(agent=road_transportation_agent)

# Main ESG Orchestrator Agent with all sub-agents
root_agent = Agent(
    name="ESG_Agent",
    model= LiteLlm(model="openai/gpt-4o-mini"),
    description="An agent that provides comprehensive ESG and SASB standards information across all industries",
    instruction= open("Prompts/esg.md").read(),
    tools = [
        file_search,
        industry_finder_agent_tool,
        apparel_accessories_footwear_agent_tool,
        appliance_manufacturing_agent_tool,
        building_products_furnishings_agent_tool,
        e_commerce_agent_tool,
        household_personal_products_agent_tool,
        multi_retail_dist_agent_tool,
        toys_sporting_goods_agent_tool,
        coal_operations_agent_tool,
        construction_materials_agent_tool,
        iron_steel_producers_agent_tool,
        metals_mining_agent_tool,
        oil_gas_exploration_production_agent_tool,
        oil_gas_midstream_agent_tool,
        oil_gas_refining_marketing_agent_tool,
        oil_gas_services_agent_tool,
        asset_management_custody_activities_agent_tool,
        commercial_banks_agent_tool,
        consumer_finance_agent_tool,
        insurance_agent_tool,
        investment_banking_brokerage_agent_tool,
        mortgage_finance_agent_tool,
        security_commodity_exchanges_agent_tool,
        agricultural_products_agent_tool,
        alcoholic_beverages_agent_tool,
        food_retailers_distributors_agent_tool,
        meat_poultry_dairy_agent_tool,
        non_alcoholic_beverages_agent_tool,
        processed_foods_agent_tool,
        restaurants_agent_tool,
        tobacco_agent_tool,
        biotechnology_pharmaceuticals_agent_tool,
        drug_retailers_agent_tool,
        health_care_delivery_agent_tool,
        health_care_distributors_agent_tool,
        managed_care_agent_tool,
        medical_equipment_supplies_agent_tool,
        electric_utilities_power_generators_agent_tool,
        engineering_construction_services_agent_tool,
        gas_utilities_distributors_agent_tool,
        home_builders_agent_tool,
        real_estate_agent_tool,
        real_estate_services_agent_tool,
        waste_management_agent_tool,
        water_utilities_services_agent_tool,
        biofuels_agent_tool,
        forestry_management_agent_tool,
        fuel_cells_industrial_batteries_agent_tool,
        pulp_paper_products_agent_tool,
        solar_technology_project_developers_agent_tool,
        wind_technology_project_developers_agent_tool,
        aerospace_defence_agent_tool,
        chemicals_agent_tool,
        containers_packaging_agent_tool,
        electrical_electronic_equipment_agent_tool,
        industrial_machinery_goods_agent_tool,
        advertising_marketing_agent_tool,
        casinos_gaming_agent_tool,
        education_agent_tool,
        hotels_lodging_agent_tool,
        leisure_facilities_agent_tool,
        media_entertainment_agent_tool,
        professional_commercial_services_agent_tool,
        elec_mfg_odm_agent_tool,
        hardware_agent_tool,
        internet_media_services_agent_tool,
        semiconductors_agent_tool,
        software_it_services_agent_tool,
        telecommunication_services_agent_tool,
        air_freight_logistics_agent_tool,
        airlines_agent_tool,
        auto_parts_agent_tool,
        automobiles_agent_tool,
        car_rental_leasing_agent_tool,
        cruise_lines_agent_tool,
        marine_transportation_agent_tool,
        rail_transportation_agent_tool,
        road_transportation_agent_tool,
    ]
)
