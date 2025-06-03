# SASB Industry Standards Agent Prompts

This directory contains prompts for a complete multi-agent SASB-based ESG reporting workflow covering all 77 SASB industries across 11 sectors.

## System Overview

The system follows a hierarchical structure with:
- **ESG Agent (Orchestrator)**: Main entry point that routes queries and coordinates responses
- **Industry Finder Agent**: Classifies companies into SASB industries using SICS methodology
- **77 Industry Standards Agents**: Specialized agents for each SASB industry standard

## Complete Industry Coverage

### Consumer Goods Sector (7 Industries)
- `apparel_accessories_footwear.md` - Apparel, Accessories & Footwear (CG-AA)
- `appliance_manufacturing.md` - Appliance Manufacturing (CG-AM)
- `building_products_furnishings.md` - Building Products & Furnishings (CG-BP)
- `e_commerce.md` - E-Commerce (CG-EC)
- `household_personal_products.md` - Household & Personal Products (CG-HP)
- `multiline_specialty_retailers_distributors.md` - Multiline and Specialty Retailers & Distributors (CG-MR)
- `toys_sporting_goods.md` - Toys & Sporting Goods (CG-TS)

### Extractives & Minerals Processing Sector (8 Industries)
- `coal_operations.md` - Coal Operations (EM-CO)
- `construction_materials.md` - Construction Materials (EM-CM)
- `iron_steel_producers.md` - Iron & Steel Producers (EM-IS)
- `metals_mining.md` - Metals & Mining (EM-MM)
- `oil_gas_exploration_production.md` - Oil & Gas – Exploration & Production (EM-EP)
- `oil_gas_midstream.md` - Oil & Gas – Midstream (EM-MD)
- `oil_gas_refining_marketing.md` - Oil & Gas – Refining & Marketing (EM-RM)
- `oil_gas_services.md` - Oil & Gas – Services (EM-SV)

### Financials Sector (7 Industries)
- `asset_management_custody_activities.md` - Asset Management & Custody Activities (FN-AC)
- `commercial_banks.md` - Commercial Banks (FN-CB)
- `consumer_finance.md` - Consumer Finance (FN-CF)
- `insurance.md` - Insurance (FN-IN)
- `investment_banking_brokerage.md` - Investment Banking & Brokerage (FN-IB)
- `mortgage_finance.md` - Mortgage Finance (FN-MF)
- `security_commodity_exchanges.md` - Security & Commodity Exchanges (FN-EX)

### Food & Beverage Sector (8 Industries)
- `agricultural_products.md` - Agricultural Products (FB-AG)
- `alcoholic_beverages.md` - Alcoholic Beverages (FB-AB)
- `food_retailers_distributors.md` - Food Retailers & Distributors (FB-FR)
- `meat_poultry_dairy.md` - Meat, Poultry & Dairy (FB-MP)
- `non_alcoholic_beverages.md` - Non-Alcoholic Beverages (FB-NB)
- `processed_foods.md` - Processed Foods (FB-PF)
- `restaurants.md` - Restaurants (FB-RN)
- `tobacco.md` - Tobacco (FB-TC)

### Health Care Sector (6 Industries)
- `biotechnology_pharmaceuticals.md` - Biotechnology & Pharmaceuticals (HC-BP)
- `drug_retailers.md` - Drug Retailers (HC-DR)
- `health_care_delivery.md` - Health Care Delivery (HC-DL)
- `health_care_distributors.md` - Health Care Distributors (HC-DI)
- `managed_care.md` - Managed Care (HC-MC)
- `medical_equipment_supplies.md` - Medical Equipment & Supplies (HC-MS)

### Infrastructure Sector (8 Industries)
- `electric_utilities_power_generators.md` - Electric Utilities & Power Generators (IF-EU)
- `engineering_construction_services.md` - Engineering & Construction Services (IF-EN)
- `gas_utilities_distributors.md` - Gas Utilities & Distributors (IF-GU)
- `home_builders.md` - Home Builders (IF-HB)
- `real_estate.md` - Real Estate (IF-RE)
- `real_estate_services.md` - Real Estate Services (IF-RS)
- `waste_management.md` - Waste Management (IF-WM)
- `water_utilities_services.md` - Water Utilities & Services (IF-WU)

### Renewable Resources & Alternative Energy Sector (6 Industries)
- `biofuels.md` - Biofuels (RR-BI)
- `forestry_management.md` - Forestry Management (RR-FM)
- `fuel_cells_industrial_batteries.md` - Fuel Cells & Industrial Batteries (RR-FB)
- `pulp_paper_products.md` - Pulp & Paper Products (RR-PP)
- `solar_technology_project_developers.md` - Solar Technology & Project Developers (RR-ST)
- `wind_technology_project_developers.md` - Wind Technology & Project Developers (RR-WT)

### Resource Transformation Sector (5 Industries)
- `aerospace_defence.md` - Aerospace & Defence (RT-AE)
- `chemicals.md` - Chemicals (RT-CH)
- `containers_packaging.md` - Containers & Packaging (RT-CP)
- `electrical_electronic_equipment.md` - Electrical & Electronic Equipment (RT-EE)
- `industrial_machinery_goods.md` - Industrial Machinery & Goods (RT-IG)

### Services Sector (7 Industries)
- `advertising_marketing.md` - Advertising & Marketing (SV-AD)
- `casinos_gaming.md` - Casinos & Gaming (SV-CA)
- `education.md` - Education (SV-ED)
- `hotels_lodging.md` - Hotels & Lodging (SV-HL)
- `leisure_facilities.md` - Leisure Facilities (SV-LF)
- `media_entertainment.md` - Media & Entertainment (SV-ME)
- `professional_commercial_services.md` - Professional & Commercial Services (SV-PS)

### Technology & Communications Sector (6 Industries)
- `electronic_manufacturing_services_odm.md` - Electronic Manufacturing Services & Original Design Manufacturing (TC-ES)
- `hardware.md` - Hardware (TC-HW)
- `internet_media_services.md` - Internet Media & Services (TC-IM)
- `semiconductors.md` - Semiconductors (TC-SC)
- `software_it_services.md` - Software & IT Services (TC-SI)
- `telecommunication_services.md` - Telecommunication Services (TC-TL)

### Transportation Sector (9 Industries)
- `air_freight_logistics.md` - Air Freight & Logistics (TR-AF)
- `airlines.md` - Airlines (TR-AL)
- `auto_parts.md` - Auto Parts (TR-AP)
- `automobiles.md` - Automobiles (TR-AU)
- `car_rental_leasing.md` - Car Rental & Leasing (TR-CR)
- `cruise_lines.md` - Cruise Lines (TR-CL)
- `marine_transportation.md` - Marine Transportation (TR-MT)
- `rail_transportation.md` - Rail Transportation (TR-RA)
- `road_transportation.md` - Road Transportation (TR-RO)

## System Coordination Files

- `esg.md` - Main ESG Agent (Orchestrator) that routes queries to appropriate specialized agents
- `industry_finder.md` - Industry Classification Agent using SICS methodology

## Architecture

Each industry-specific agent follows a consistent structure:
- **Role**: Industry expert for specific SASB standard
- **Task**: Semantic search and synthesis from industry-specific SASB documents
- **Input**: Free-form sustainability questions for that industry
- **Output**: Authoritative SASB disclosure topics, metrics, and guidance
- **Constrictions**: Single source of truth, exact language reproduction, no speculation
- **Capabilities**: Direct links to official SASB PDFs for each industry

## Usage

The system is designed for comprehensive ESG/SASB sustainability reporting workflows where:
1. Users submit queries to the ESG Agent (Orchestrator)
2. Queries are classified and routed to appropriate industry experts
3. Industry agents provide authoritative SASB-based responses
4. Cross-industry queries are handled directly by the orchestrator

**Total Coverage**: 79 prompt files covering all 77 SASB industries plus coordination agents

Created: January 2025