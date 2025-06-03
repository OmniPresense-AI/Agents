# SASB Industry Agents Index

This directory contains agents for all 77 SASB industries plus coordination agents.

## System Architecture

### Orchestrator Agents
- **ESG Agent**: Main coordination agent that routes queries to appropriate industry experts
- **Industry Finder Agent**: Classifies companies into SASB industries using SICS methodology

### Industry-Specific Agents (77 total)

#### Consumer Goods Sector (7 industries)
- **Apparel, Accessories & Footwear** (`CG-AA`) - `agents/apparel_accessories_footwear/`
- **Appliance Manufacturing** (`CG-AM`) - `agents/appliance_manufacturing/`
- **Building Products & Furnishings** (`CG-BP`) - `agents/building_products_furnishings/`
- **E-Commerce** (`CG-EC`) - `agents/e_commerce/`
- **Household & Personal Products** (`CG-HP`) - `agents/household_personal_products/`
- **Multiline and Specialty Retailers & Distributors** (`CG-MR`) - `agents/multiline_specialty_retailers_distributors/`
- **Toys & Sporting Goods** (`CG-TS`) - `agents/toys_sporting_goods/`

#### Extractives & Minerals Processing Sector (8 industries)
- **Coal Operations** (`EM-CO`) - `agents/coal_operations/`
- **Construction Materials** (`EM-CM`) - `agents/construction_materials/`
- **Iron & Steel Producers** (`EM-IS`) - `agents/iron_steel_producers/`
- **Metals & Mining** (`EM-MM`) - `agents/metals_mining/`
- **Oil & Gas – Exploration & Production** (`EM-EP`) - `agents/oil_gas_exploration_production/`
- **Oil & Gas – Midstream** (`EM-MD`) - `agents/oil_gas_midstream/`
- **Oil & Gas – Refining & Marketing** (`EM-RM`) - `agents/oil_gas_refining_marketing/`
- **Oil & Gas – Services** (`EM-SV`) - `agents/oil_gas_services/`

#### Financials Sector (7 industries)
- **Asset Management & Custody Activities** (`FN-AC`) - `agents/asset_management_custody_activities/`
- **Commercial Banks** (`FN-CB`) - `agents/commercial_banks/`
- **Consumer Finance** (`FN-CF`) - `agents/consumer_finance/`
- **Insurance** (`FN-IN`) - `agents/insurance/`
- **Investment Banking & Brokerage** (`FN-IB`) - `agents/investment_banking_brokerage/`
- **Mortgage Finance** (`FN-MF`) - `agents/mortgage_finance/`
- **Security & Commodity Exchanges** (`FN-EX`) - `agents/security_commodity_exchanges/`

#### Food & Beverage Sector (8 industries)
- **Agricultural Products** (`FB-AG`) - `agents/agricultural_products/`
- **Alcoholic Beverages** (`FB-AB`) - `agents/alcoholic_beverages/`
- **Food Retailers & Distributors** (`FB-FR`) - `agents/food_retailers_distributors/`
- **Meat, Poultry & Dairy** (`FB-MP`) - `agents/meat_poultry_dairy/`
- **Non-Alcoholic Beverages** (`FB-NB`) - `agents/non_alcoholic_beverages/`
- **Processed Foods** (`FB-PF`) - `agents/processed_foods/`
- **Restaurants** (`FB-RN`) - `agents/restaurants/`
- **Tobacco** (`FB-TC`) - `agents/tobacco/`

#### Health Care Sector (6 industries)
- **Biotechnology & Pharmaceuticals** (`HC-BP`) - `agents/biotechnology_pharmaceuticals/`
- **Drug Retailers** (`HC-DR`) - `agents/drug_retailers/`
- **Health Care Delivery** (`HC-DL`) - `agents/health_care_delivery/`
- **Health Care Distributors** (`HC-DI`) - `agents/health_care_distributors/`
- **Managed Care** (`HC-MC`) - `agents/managed_care/`
- **Medical Equipment & Supplies** (`HC-MS`) - `agents/medical_equipment_supplies/`

#### Infrastructure Sector (8 industries)
- **Electric Utilities & Power Generators** (`IF-EU`) - `agents/electric_utilities_power_generators/`
- **Engineering & Construction Services** (`IF-EN`) - `agents/engineering_construction_services/`
- **Gas Utilities & Distributors** (`IF-GU`) - `agents/gas_utilities_distributors/`
- **Home Builders** (`IF-HB`) - `agents/home_builders/`
- **Real Estate** (`IF-RE`) - `agents/real_estate/`
- **Real Estate Services** (`IF-RS`) - `agents/real_estate_services/`
- **Waste Management** (`IF-WM`) - `agents/waste_management/`
- **Water Utilities & Services** (`IF-WU`) - `agents/water_utilities_services/`

#### Renewable Resources & Alternative Energy Sector (6 industries)
- **Biofuels** (`RR-BI`) - `agents/biofuels/`
- **Forestry Management** (`RR-FM`) - `agents/forestry_management/`
- **Fuel Cells & Industrial Batteries** (`RR-FB`) - `agents/fuel_cells_industrial_batteries/`
- **Pulp & Paper Products** (`RR-PP`) - `agents/pulp_paper_products/`
- **Solar Technology & Project Developers** (`RR-ST`) - `agents/solar_technology_project_developers/`
- **Wind Technology & Project Developers** (`RR-WT`) - `agents/wind_technology_project_developers/`

#### Resource Transformation Sector (5 industries)
- **Aerospace & Defence** (`RT-AE`) - `agents/aerospace_defence/`
- **Chemicals** (`RT-CH`) - `agents/chemicals/`
- **Containers & Packaging** (`RT-CP`) - `agents/containers_packaging/`
- **Electrical & Electronic Equipment** (`RT-EE`) - `agents/electrical_electronic_equipment/`
- **Industrial Machinery & Goods** (`RT-IG`) - `agents/industrial_machinery_goods/`

#### Services Sector (7 industries)
- **Advertising & Marketing** (`SV-AD`) - `agents/advertising_marketing/`
- **Casinos & Gaming** (`SV-CA`) - `agents/casinos_gaming/`
- **Education** (`SV-ED`) - `agents/education/`
- **Hotels & Lodging** (`SV-HL`) - `agents/hotels_lodging/`
- **Leisure Facilities** (`SV-LF`) - `agents/leisure_facilities/`
- **Media & Entertainment** (`SV-ME`) - `agents/media_entertainment/`
- **Professional & Commercial Services** (`SV-PS`) - `agents/professional_commercial_services/`

#### Technology & Communications Sector (6 industries)
- **Electronic Manufacturing Services & Original Design Manufacturing** (`TC-ES`) - `agents/electronic_manufacturing_services_odm/`
- **Hardware** (`TC-HW`) - `agents/hardware/`
- **Internet Media & Services** (`TC-IM`) - `agents/internet_media_services/`
- **Semiconductors** (`TC-SC`) - `agents/semiconductors/`
- **Software & IT Services** (`TC-SI`) - `agents/software_it_services/`
- **Telecommunication Services** (`TC-TL`) - `agents/telecommunication_services/`

#### Transportation Sector (9 industries)
- **Air Freight & Logistics** (`TR-AF`) - `agents/air_freight_logistics/`
- **Airlines** (`TR-AL`) - `agents/airlines/`
- **Auto Parts** (`TR-AP`) - `agents/auto_parts/`
- **Automobiles** (`TR-AU`) - `agents/automobiles/`
- **Car Rental & Leasing** (`TR-CR`) - `agents/car_rental_leasing/`
- **Cruise Lines** (`TR-CL`) - `agents/cruise_lines/`
- **Marine Transportation** (`TR-MT`) - `agents/marine_transportation/`
- **Rail Transportation** (`TR-RA`) - `agents/rail_transportation/`
- **Road Transportation** (`TR-RO`) - `agents/road_transportation/`


## Usage

Each agent directory contains:
- `agent.py` - Agent definition with model, tools, and instructions
- `__init__.py` - Python package initialization

## Integration

All agents use:
- **Model**: `openai/gpt-4o-mini` via LiteLLM
- **Tools**: `file_search` (comprehensive SASB standards RAG system)
- **Instructions**: Industry-specific prompts from `Prompts/` directory

## Created

Total agents: 79 (77 industries + 2 coordination agents)
Generated: /home/musili/Agents
