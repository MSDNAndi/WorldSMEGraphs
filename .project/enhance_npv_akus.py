#!/usr/bin/env python3
"""
Enhance NPV AKUs with ontology annotations based on researched identifiers.
"""

import json
import sys
from pathlib import Path
from datetime import datetime

# Ontology mappings from research
ONTOLOGY_MAPPINGS = {
    "npv": {
        "skos:prefLabel": "Net Present Value",
        "skos:altLabel": ["NPV", "Nettobarwert", "VAN"],
        "owl:sameAs": "https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/NetPresentValue",
        "skos:exactMatch": [
            "https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/NetPresentValue",
            "http://dbpedia.org/resource/Net_present_value",
            "http://www.wikidata.org/entity/Q1054308"
        ]
    },
    "present-value": {
        "skos:prefLabel": "Present Value",
        "skos:altLabel": ["PV", "Barwert", "valeur actuelle"],
        "owl:sameAs": "https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/PresentValue",
        "skos:exactMatch": [
            "https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/PresentValue",
            "http://dbpedia.org/resource/Present_value",
            "http://www.wikidata.org/entity/Q332099"
        ]
    },
    "discount-rate": {
        "skos:prefLabel": "Discount Rate",
        "skos:altLabel": ["Required Rate of Return", "Hurdle Rate", "Cost of Capital"],
        "owl:sameAs": "https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/DiscountRate",
        "skos:exactMatch": [
            "https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/DiscountRate"
        ],
        "skos:broadMatch": [
            "http://dbpedia.org/resource/Discount_rate",
            "http://www.wikidata.org/entity/Q1226339"
        ],
        "skos:closeMatch": [
            "http://www.wikidata.org/entity/Q899651"
        ]
    },
    "cash-flow": {
        "skos:prefLabel": "Cash Flow",
        "skos:altLabel": ["Cashflow", "Geldfluss", "flujo de efectivo"],
        "owl:sameAs": "https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/CashFlow",
        "skos:exactMatch": [
            "https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/CashFlow",
            "http://dbpedia.org/resource/Cash_flow",
            "http://www.wikidata.org/entity/Q223557"
        ]
    },
    "discount-factor": {
        "skos:prefLabel": "Discount Factor",
        "owl:sameAs": "https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/DiscountFactor",
        "skos:exactMatch": [
            "https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/DiscountFactor",
            "http://www.wikidata.org/entity/Q5281138"
        ],
        "skos:closeMatch": [
            "http://dbpedia.org/resource/Discounting#Discount_factor"
        ]
    },
    "time-value-of-money": {
        "skos:prefLabel": "Time Value of Money",
        "skos:altLabel": ["TVM", "Zeitwert des Geldes"],
        "owl:sameAs": "https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/TimeValueOfMoney",
        "skos:exactMatch": [
            "https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/TimeValueOfMoney",
            "http://dbpedia.org/resource/Time_value_of_money",
            "http://www.wikidata.org/entity/Q1200790"
        ]
    }
}

def detect_concept(aku_id, content):
    """Detect which concept this AKU represents."""
    aku_id_lower = aku_id.lower()
    
    if "npv" in aku_id_lower and "definition" in aku_id_lower:
        return "npv"
    elif "present-value" in aku_id_lower or "present value" in str(content).lower()[:200]:
        return "present-value"
    elif "discount-rate" in aku_id_lower or "discount rate" in str(content).lower()[:200]:
        return "discount-rate"
    elif "cash-flow" in aku_id_lower or "cash flow" in str(content).lower()[:200]:
        return "cash-flow"
    elif "discount-factor" in aku_id_lower or "discount factor" in str(content).lower()[:200]:
        return "discount-factor"
    
    # Default for formulas/examples
    return "npv"

def enhance_aku(aku_path: Path) -> bool:
    """Enhance a single AKU with ontology annotations."""
    try:
        with open(aku_path, 'r', encoding='utf-8') as f:
            aku = json.load(f)
        
        # Update @context
        aku["@context"] = [
            "file://domain/_contexts/base.jsonld",
            "file://domain/_contexts/economics.jsonld"
        ]
        
        # Detect concept
        concept = detect_concept(aku.get("@id", ""), aku.get("content", {}))
        mappings = ONTOLOGY_MAPPINGS.get(concept, ONTOLOGY_MAPPINGS["npv"])
        
        # Add SKOS properties
        if "skos:prefLabel" not in aku:
            aku["skos:prefLabel"] = mappings["skos:prefLabel"]
        
        if "skos:notation" not in aku:
            aku["skos:notation"] = aku.get("@id", "")
        
        # Extract definition from content
        if "skos:definition" not in aku and "content" in aku:
            if "statement" in aku["content"]:
                stmt = aku["content"]["statement"]
                if isinstance(stmt, dict) and "text" in stmt:
                    aku["skos:definition"] = stmt["text"][:500]
                elif isinstance(stmt, str):
                    aku["skos:definition"] = stmt[:500]
        
        # Add alternative labels if available
        if "skos:altLabel" in mappings and "skos:altLabel" not in aku:
            aku["skos:altLabel"] = mappings["skos:altLabel"]
        
        # Add external ontology links
        if "owl:sameAs" not in aku:
            aku["owl:sameAs"] = mappings["owl:sameAs"]
        
        for match_type in ["skos:exactMatch", "skos:closeMatch", "skos:broadMatch"]:
            if match_type in mappings and match_type not in aku:
                aku[match_type] = mappings[match_type]
        
        # Convert relationships to SKOS format
        if "relationships" in aku:
            relationships = aku["relationships"]
            
            # Convert prerequisites to broader
            if "prerequisites" in relationships:
                if "skos:broader" not in relationships:
                    broader = []
                    for prereq in relationships["prerequisites"]:
                        if isinstance(prereq, str):
                            broader.append({"@id": f"wsmg:{prereq}", "@type": "skos:Concept"})
                        elif isinstance(prereq, dict) and "id" in prereq:
                            broader.append({"@id": prereq["id"], "@type": "skos:Concept"})
                    if broader:
                        relationships["skos:broader"] = broader
            
            # Convert enables to narrower
            if "enables" in relationships:
                if "skos:narrower" not in relationships:
                    narrower = []
                    for enable in relationships["enables"]:
                        if isinstance(enable, str):
                            narrower.append({"@id": f"wsmg:{enable}", "@type": "skos:Concept"})
                        elif isinstance(enable, dict) and "id" in enable:
                            narrower.append({"@id": enable["id"], "@type": "skos:Concept"})
                    if narrower:
                        relationships["skos:narrower"] = narrower
            
            # Convert related_to to related
            if "related_to" in relationships:
                if "skos:related" not in relationships:
                    related = []
                    for rel in relationships["related_to"]:
                        if isinstance(rel, str):
                            related.append({"@id": f"wsmg:{rel}", "@type": "skos:Concept"})
                        elif isinstance(rel, dict) and "id" in rel:
                            related.append({"@id": rel["id"], "@type": "skos:Concept"})
                    if related:
                        relationships["skos:related"] = related
        
        # Add PROV-O provenance
        if "provenance" not in aku:
            aku["provenance"] = {}
        
        provenance = aku["provenance"]
        
        # Add creation attribution
        if "dc:creator" not in provenance:
            provenance["dc:creator"] = aku.get("metadata", {}).get("contributors", ["ontology-enhancement-agent"])
        
        # Add modification timestamp
        provenance["dc:modified"] = datetime.utcnow().isoformat() + "Z"
        
        # Add derivation info
        if "prov:wasDerivedFrom" not in provenance and "sources" in provenance:
            sources_list = []
            for source in provenance.get("sources", []):
                if isinstance(source, dict):
                    source_entry = {}
                    if "citation" in source:
                        source_entry["dc:bibliographicCitation"] = source["citation"]
                    if "title" in source:
                        source_entry["dc:title"] = source["title"]
                    sources_list.append(source_entry)
            if sources_list:
                provenance["prov:wasDerivedFrom"] = sources_list
        
        # Update metadata
        if "metadata" in aku:
            aku["metadata"]["status"] = "ontology-enhanced"
            aku["metadata"]["last_updated"] = datetime.utcnow().isoformat() + "Z"
            if "contributors" in aku["metadata"]:
                if "ontology-enhancement-agent" not in aku["metadata"]["contributors"]:
                    aku["metadata"]["contributors"].append("ontology-enhancement-agent")
        
        # Write back
        with open(aku_path, 'w', encoding='utf-8') as f:
            json.dump(aku, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Enhanced: {aku_path.name}")
        return True
        
    except Exception as e:
        print(f"❌ Error enhancing {aku_path.name}: {e}")
        return False

def main():
    base_dir = Path("/home/runner/work/WorldSMEGraphs/WorldSMEGraphs/.project/pilot/npv-finance/akus")
    
    # Find all AKUs except already enhanced ones
    aku_files = []
    for subdir in ["definitions", "formulas", "examples", "theory"]:
        dir_path = base_dir / subdir
        if dir_path.exists():
            for aku_file in dir_path.glob("*.json"):
                if "ENHANCED" not in aku_file.name:
                    aku_files.append(aku_file)
    
    print(f"Enhancing {len(aku_files)} AKUs...\n")
    
    success = 0
    for aku_file in sorted(aku_files):
        if enhance_aku(aku_file):
            success += 1
    
    print(f"\n{'='*70}")
    print(f"SUMMARY")
    print(f"{'='*70}")
    print(f"Total: {len(aku_files)}")
    print(f"✅ Success: {success}")
    print(f"❌ Failed: {len(aku_files) - success}")
    
    return 0 if success == len(aku_files) else 1

if __name__ == "__main__":
    sys.exit(main())
