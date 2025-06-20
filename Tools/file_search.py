from google.adk.tools.crewai_tool import CrewaiTool
from crewai_tools import RagTool

rag_tool = RagTool()

# Upload the core documents to the vector store
rag_tool.add(data_type="pdf_file", source="Standards/SASB-Conceptual-Framework.pdf", metadata={
    "name": "SASB-Conceptual-Framework",
    "document_type": "core_document"
})
rag_tool.add(data_type="pdf_file", source="Standards/SASB-Standards-Application-Guidance-2018-10.pdf", metadata={
    "name": "SASB-Standards-Application-Guidance-2018-10",
    "document_type": "core_document"
})
rag_tool.add(data_type="pdf_file", source="Standards/sasb-taxonomy-2024-11-07.pdf", metadata={
    "name": "sasb-taxonomy-2024-11-07",
    "document_type": "core_document"
})
rag_tool.add(data_type="json", source="Standards/SASB_Industry_Data.json", metadata={
    "name": "SASB_Industry_Data",
    "document_type": "industry_mapping"
})

# Industry PDF metadata mapping (sector, industry, file, version)
industry_metadata = [
    # Consumer Goods
    {"industry_name": "Apparel, Accessories & Footwear", "sector_name": "Consumer Goods", "file_name": "apparel-accessories-and-footwear-standard_en-gb.pdf"},
    {"industry_name": "Appliance Manufacturing", "sector_name": "Consumer Goods", "file_name": "appliance-manufacturing-standard_en-gb.pdf"},
    {"industry_name": "Building Products & Furnishings", "sector_name": "Consumer Goods", "file_name": "building-products-and-furnishings-standard_en-gb.pdf"},
    {"industry_name": "E-Commerce", "sector_name": "Consumer Goods", "file_name": "e-commerce-standard_en-gb.pdf"},
    {"industry_name": "Household & Personal Products", "sector_name": "Consumer Goods", "file_name": "household-and-personal-products-standard_en-gb.pdf"},
    {"industry_name": "Multiline and Specialty Retailers & Distributors", "sector_name": "Consumer Goods", "file_name": "multiline-and-specialty-retailers-and-distributors-standard_en-gb.pdf"},
    {"industry_name": "Toys & Sporting Goods", "sector_name": "Consumer Goods", "file_name": "toys-and-sporting-goods-standard_en-gb.pdf"},
    # Extractives & Minerals Processing
    {"industry_name": "Coal Operations", "sector_name": "Extractives & Minerals Processing", "file_name": "coal-operations-standard_en-gb.pdf"},
    {"industry_name": "Construction Materials", "sector_name": "Extractives & Minerals Processing", "file_name": "construction-materials-standard_en-gb.pdf"},
    {"industry_name": "Iron & Steel Producers", "sector_name": "Extractives & Minerals Processing", "file_name": "iron-and-steel-producers-standard_en-gb.pdf"},
    {"industry_name": "Metals & Mining", "sector_name": "Extractives & Minerals Processing", "file_name": "metals-and-mining-standard_en-gb.pdf"},
    {"industry_name": "Oil & Gas – Exploration & Production", "sector_name": "Extractives & Minerals Processing", "file_name": "oil-and-gas-exploration-and-production-standard_en-gb.pdf"},
    {"industry_name": "Oil & Gas – Midstream", "sector_name": "Extractives & Minerals Processing", "file_name": "oil-and-gas-midstream-standard_en-gb.pdf"},
    {"industry_name": "Oil & Gas – Refining & Marketing", "sector_name": "Extractives & Minerals Processing", "file_name": "oil-and-gas-refining-and-marketing-standard_en-gb.pdf"},
    {"industry_name": "Oil & Gas – Services", "sector_name": "Extractives & Minerals Processing", "file_name": "oil-and-gas-services-standard_en-gb.pdf"},
    # Financials
    {"industry_name": "Asset Management & Custody Activities", "sector_name": "Financials", "file_name": "asset-management-and-custody-activities-standard_en-gb.pdf"},
    {"industry_name": "Commercial Banks", "sector_name": "Financials", "file_name": "commercial-banks-standard_en-gb.pdf"},
    {"industry_name": "Consumer Finance", "sector_name": "Financials", "file_name": "consumer-finance-standard_en-gb.pdf"},
    {"industry_name": "Insurance", "sector_name": "Financials", "file_name": "insurance-standard_en-gb.pdf"},
    {"industry_name": "Investment Banking & Brokerage", "sector_name": "Financials", "file_name": "investment-banking-and-brokerage-standard_en-gb.pdf"},
    {"industry_name": "Mortgage Finance", "sector_name": "Financials", "file_name": "mortgage-finance-standard_en-gb.pdf"},
    {"industry_name": "Security & Commodity Exchanges", "sector_name": "Financials", "file_name": "security-and-commodity-exchanges-standard_en-gb.pdf"},
    # Food & Beverage
    {"industry_name": "Agricultural Products", "sector_name": "Food & Beverage", "file_name": "agricultural-products-standard_en-gb.pdf"},
    {"industry_name": "Alcoholic Beverages", "sector_name": "Food & Beverage", "file_name": "alcoholic-beverages-standard_en-gb.pdf"},
    {"industry_name": "Food Retailers & Distributors", "sector_name": "Food & Beverage", "file_name": "food-retailers-and-distributors-standard_en-gb.pdf"},
    {"industry_name": "Meat, Poultry & Dairy", "sector_name": "Food & Beverage", "file_name": "meat-poultry-and-dairy-standard_en-gb.pdf"},
    {"industry_name": "Non-Alcoholic Beverages", "sector_name": "Food & Beverage", "file_name": "non-alcoholic-beverages-standard_en-gb.pdf"},
    {"industry_name": "Processed Foods", "sector_name": "Food & Beverage", "file_name": "processed-foods-standard_en-gb.pdf"},
    {"industry_name": "Restaurants", "sector_name": "Food & Beverage", "file_name": "restaurants-standard_en-gb.pdf"},
    {"industry_name": "Tobacco", "sector_name": "Food & Beverage", "file_name": "tobacco-standard_en-gb.pdf"},
    # Health Care
    {"industry_name": "Biotechnology & Pharmaceuticals", "sector_name": "Health Care", "file_name": "biotechnology-and-pharmaceuticals-standard_en-gb.pdf"},
    {"industry_name": "Drug Retailers", "sector_name": "Health Care", "file_name": "drug-retailers-standard_en-gb.pdf"},
    {"industry_name": "Health Care Delivery", "sector_name": "Health Care", "file_name": "health-care-delivery-standard_en-gb.pdf"},
    {"industry_name": "Health Care Distributors", "sector_name": "Health Care", "file_name": "health-care-distributors-standard_en-gb.pdf"},
    {"industry_name": "Managed Care", "sector_name": "Health Care", "file_name": "managed-care-standard_en-gb.pdf"},
    {"industry_name": "Medical Equipment & Supplies", "sector_name": "Health Care", "file_name": "medical-equipment-and-supplies-standard_en-gb.pdf"},
    # Infrastructure
    {"industry_name": "Electric Utilities & Power Generators", "sector_name": "Infrastructure", "file_name": "electric-utilities-and-power-generators-standard_en-gb.pdf"},
    {"industry_name": "Engineering & Construction Services", "sector_name": "Infrastructure", "file_name": "engineering-and-construction-services-standard_en-gb.pdf"},
    {"industry_name": "Gas Utilities & Distributors", "sector_name": "Infrastructure", "file_name": "gas-utilities-and-distributors-standard_en-gb.pdf"},
    {"industry_name": "Home Builders", "sector_name": "Infrastructure", "file_name": "home-builders-standard_en-gb.pdf"},
    {"industry_name": "Real Estate", "sector_name": "Infrastructure", "file_name": "real-estate-standard_en-gb.pdf"},
    {"industry_name": "Real Estate Services", "sector_name": "Infrastructure", "file_name": "real-estate-services-standard_en-gb.pdf"},
    {"industry_name": "Waste Management", "sector_name": "Infrastructure", "file_name": "waste-management-standard_en-gb.pdf"},
    {"industry_name": "Water Utilities & Services", "sector_name": "Infrastructure", "file_name": "water-utilities-and-services-standard_en-gb.pdf"},
    # Renewable Resources & Alternative Energy
    {"industry_name": "Biofuels", "sector_name": "Renewable Resources & Alternative Energy", "file_name": "biofuels-standard_en-gb.pdf"},
    {"industry_name": "Forestry Management", "sector_name": "Renewable Resources & Alternative Energy", "file_name": "forestry-management-standard_en-gb.pdf"},
    {"industry_name": "Fuel Cells & Industrial Batteries", "sector_name": "Renewable Resources & Alternative Energy", "file_name": "fuel-cells-and-industrial-batteries-standard_en-gb.pdf"},
    {"industry_name": "Pulp & Paper Products", "sector_name": "Renewable Resources & Alternative Energy", "file_name": "pulp-and-paper-products-standard_en-gb.pdf"},
    {"industry_name": "Solar Technology & Project Developers", "sector_name": "Renewable Resources & Alternative Energy", "file_name": "solar-technology-and-project-developers-standard_en-gb.pdf"},
    {"industry_name": "Wind Technology & Project Developers", "sector_name": "Renewable Resources & Alternative Energy", "file_name": "wind-technology-and-project-developers-standard_en-gb.pdf"},
    # Resource Transformation
    {"industry_name": "Aerospace & Defence", "sector_name": "Resource Transformation", "file_name": "aerospace-and-defence-standard_en-gb.pdf"},
    {"industry_name": "Chemicals", "sector_name": "Resource Transformation", "file_name": "chemicals-standard_en-gb.pdf"},
    {"industry_name": "Containers & Packaging", "sector_name": "Resource Transformation", "file_name": "containers-and-packaging-standard_en-gb.pdf"},
    {"industry_name": "Electrical & Electronic Equipment", "sector_name": "Resource Transformation", "file_name": "electrical-and-electronic-equipment-standard_en-gb.pdf"},
    {"industry_name": "Industrial Machinery & Goods", "sector_name": "Resource Transformation", "file_name": "industrial-machinery-and-goods-standard_en-gb.pdf"},
    # Services
    {"industry_name": "Advertising & Marketing", "sector_name": "Services", "file_name": "advertising-and-marketing-standard_en-gb.pdf"},
    {"industry_name": "Casinos & Gaming", "sector_name": "Services", "file_name": "casinos-and-gaming-standard_en-gb.pdf"},
    {"industry_name": "Education", "sector_name": "Services", "file_name": "education-standard_en-gb.pdf"},
    {"industry_name": "Hotels & Lodging", "sector_name": "Services", "file_name": "hotels-and-lodging-standard_en-gb.pdf"},
    {"industry_name": "Leisure Facilities", "sector_name": "Services", "file_name": "leisure-facilities-standard_en-gb.pdf"},
    {"industry_name": "Media & Entertainment", "sector_name": "Services", "file_name": "media-and-entertainment-standard_en-gb.pdf"},
    {"industry_name": "Professional & Commercial Services", "sector_name": "Services", "file_name": "professional-and-commercial-services-standard_en-gb.pdf"},
    # Technology & Communications
    {"industry_name": "Electronic Manufacturing Services & Original Design Manufacturing", "sector_name": "Technology & Communications", "file_name": "electronic-manufacturing-services-and-original-design-manufacturing-standard_en-gb.pdf"},
    {"industry_name": "Hardware", "sector_name": "Technology & Communications", "file_name": "hardware-standard_en-gb.pdf"},
    {"industry_name": "Internet Media & Services", "sector_name": "Technology & Communications", "file_name": "internet-media-and-services-standard_en-gb.pdf"},
    {"industry_name": "Semiconductors", "sector_name": "Technology & Communications", "file_name": "semiconductors-standard_en-gb.pdf"},
    {"industry_name": "Software & IT Services", "sector_name": "Technology & Communications", "file_name": "software-and-it-services-standard_en-gb.pdf"},
    {"industry_name": "Telecommunication Services", "sector_name": "Technology & Communications", "file_name": "telecommunication-services-standard_en-gb.pdf"},
    # Transportation
    {"industry_name": "Air Freight & Logistics", "sector_name": "Transportation", "file_name": "air-freight-and-logistics-standard_en-gb.pdf"},
    {"industry_name": "Airlines", "sector_name": "Transportation", "file_name": "airlines-standard_en-gb.pdf"},
    {"industry_name": "Auto Parts", "sector_name": "Transportation", "file_name": "auto-parts-standard_en-gb.pdf"},
    {"industry_name": "Automobiles", "sector_name": "Transportation", "file_name": "automobiles-standard_en-gb.pdf"},
    {"industry_name": "Car Rental & Leasing", "sector_name": "Transportation", "file_name": "car-rental-and-leasing-standard_en-gb.pdf"},
    {"industry_name": "Cruise Lines", "sector_name": "Transportation", "file_name": "cruise-lines-standard_en-gb.pdf"},
    {"industry_name": "Marine Transportation", "sector_name": "Transportation", "file_name": "marine-transportation-standard_en-gb.pdf"},
    {"industry_name": "Rail Transportation", "sector_name": "Transportation", "file_name": "rail-transportation-standard_en-gb.pdf"},
    {"industry_name": "Road Transportation", "sector_name": "Transportation", "file_name": "road-transportation-standard_en-gb.pdf"},
]

for meta in industry_metadata:
    rag_tool.add(
        data_type="pdf_file",
        source=f"Standards/{meta['file_name']}",
        metadata={
            "industry_name": meta["industry_name"],
            "sector_name": meta["sector_name"],
            "file_name": meta["file_name"],
            "version": "2023-12",
            "document_type": "industry_standard"
        }
    )

file_search = CrewaiTool(
    name="file_search",
    description="Performs a semantic search over the complete SASB standards library including all 77 industry standards, SASB Conceptual Framework, Application Guidance, Taxonomy, and industry classification data. Use this tool to find specific information or answer questions based on the content of these comprehensive sustainability disclosure standards.",
    tool=rag_tool
)
