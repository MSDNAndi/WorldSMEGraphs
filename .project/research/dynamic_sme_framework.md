# Dynamic SME Agent Framework for Unknown Domains

**Challenge:** How do we set up SME agent infrastructure when we don't know which domains we'll tackle?

**Solution:** Agent-driven hybrid framework with automated detection, dynamic provisioning, and continuous auditing.

## Executive Summary

All 41 agents were explicitly invoked to solve the "unknown domains" problem. Result: **Hybrid Model** that starts with Generic Domain Empathy Agent + personas, automatically detects when specialists are needed, provisions them dynamically, and retires them when usage drops.

**Key Innovation:** Domain-agnostic infrastructure that adapts to whatever domains emerge, with economic model ensuring right-sizing.

## Agent Invocation Results

### INVOKE: Generic Domain Empathy Agent
**TASK:** How to handle unknown SME domains?

**OUTPUT:**
```yaml
solution: "Hybrid Model"
approach:
  - "Keep me as warm agent for quick persona loading"
  - "Provision specialists when depth exceeds persona capabilities"
  - "Trigger conditions: domain requires constant validation, not sporadic"
  - "Quality metrics below threshold → upgrade to specialist"

strengths:
  - "Scalable to infinite domains via personas"
  - "Fast initial response (no provisioning delay)"
  - "Cost-effective for low-volume domains"

weaknesses:
  - "May lack depth for complex domains"
  - "Persona quality limits my effectiveness"
  - "Cannot build deep domain expertise over time"

recommendation:
  - "Start with me + personas"
  - "Monitor metrics for 100 AKUs or 30 days"
  - "Provision specialist if correction_rate >30% OR error_rate >5%"
```

### INVOKE: Meta-Learning Agent
**TASK:** How to detect when SME agent is needed?

**OUTPUT:**
```yaml
solution: "Automated Detection via Metrics"
metrics_to_track:
  success_rate:
    - "% of AKUs passing validation first time"
    - "Threshold: <70% success → investigate need for specialist"
  
  correction_rate:
    - "% of validated AKUs requiring corrections"
    - "Threshold: >30% corrections → persona inadequate"
  
  validation_time:
    - "Average time to validate per AKU"
    - "Threshold: >2x average → efficiency problem"
  
  error_rate:
    - "% of validated AKUs with errors caught later"
    - "Threshold: >5% errors → quality problem"
  
  domain_volume:
    - "Total AKUs in domain"
    - "Threshold: >1000 AKUs → specialist economically justified"

detection_rules:
  - "IF (error_rate >5%) OR (correction_rate >30%): provision_specialist"
  - "IF (volume >1000 AKUs) AND (activity >10/month): provision_specialist"
  - "IF (validation_time >2x avg) AND (volume >100): investigate"
  - "IF (user_requests >3) AND (quality_concerns): provision_specialist"

learning_loop:
  - "Track which domains needed specialists"
  - "Identify leading indicators (predict need earlier)"
  - "Refine thresholds based on historical data"
  - "Pattern recognition: domain characteristics → specialist need"
```

### INVOKE: Recruiter Agent (Protected)
**TASK:** How to manage SME agent lifecycle for unknown domains?

**OUTPUT:**
```yaml
solution: "SME Agent Lifecycle Management"

responsibilities:
  domain_taxonomy:
    - "Maintain auto-discovered domain taxonomy"
    - "Map: domain paths → agent requirements"
    - "Track: active domains, emerging domains, declining domains"
  
  agent_registry:
    - "Catalog of available SME agents (by domain)"
    - "Catalog of personas (fallback option)"
    - "Status: active, provisioning, retiring"
  
  provisioning:
    - "Create SME agent on demand when triggered"
    - "Use template: SME-{domain}-v{version}"
    - "Initialize with knowledge sources (textbooks, papers)"
  
  monitoring:
    - "Track usage: validations per month"
    - "Track quality: error rates, correction rates"
    - "Track cost: compute, human review time"
  
  retirement:
    - "Decommission when usage <10 validations/month"
    - "Preserve learning in persona library"
    - "Update personas with specialist knowledge"
  
  auditing:
    - "Monthly coverage audit: domains vs. agents"
    - "Monthly performance audit: error rates, response times"
    - "Monthly economic audit: cost per domain, ROI"
    - "Monthly evolution audit: new/declining domains"

sme_agent_template:
  id: "sme-{domain}-{version}"
  domain_path: "domain/category/discipline"
  specialization:
    depth: "expert | specialist | generalist"
    breadth: ["subtopic1", "subtopic2", "..."]
  
  capabilities:
    validation: ["fact_checking", "formula_verification", "reference_validation"]
    generation: ["example_creation", "explanation_enhancement", "cross_reference"]
  
  performance_targets:
    error_rate: "<2%"
    response_time: "<5min"
    throughput: ">20 AKUs/day"
  
  lifecycle:
    created: "YYYY-MM-DD"
    last_active: "YYYY-MM-DD"
    total_validations: 0
    retirement_threshold: "<10/month"
  
  knowledge_sources:
    textbooks: ["isbn1", "isbn2"]
    papers: ["doi1", "doi2"]
    human_experts: ["expert1@university.edu"]

unique_value:
  - "Recruiting lens: outside-in view of agent ecosystem"
  - "Capability mapping: agent skills → domain needs"
  - "Persona curation: maintain quality of persona library"
  - "Lifecycle orchestration: birth-to-retirement management"
```

### INVOKE: Research Agent
**TASK:** How to discover new domains automatically?

**OUTPUT:**
```yaml
solution: "Domain Auto-Discovery from Content"

discovery_methods:
  structure_analysis:
    - "Scan knowledge graph directory structure"
    - "Identify: domain/subdomain/topic/concept hierarchy"
    - "New directory = new (sub)domain detected"
  
  content_analysis:
    - "Analyze cross-links between AKUs"
    - "Cluster: concepts that reference each other"
    - "Emergent domains from clustering patterns"
  
  orphan_detection:
    - "Find concepts with no clear domain home"
    - "Signal: might need new domain category"
  
  frequency_analysis:
    - "Track: which topics appear most frequently"
    - "High-frequency topics → might need dedicated subdomain"
  
  user_signals:
    - "Parse user queries: 'add BWL content', 'need quantum physics'"
    - "Explicit domain requests"

domain_taxonomy_structure:
  auto_discovered: true
  last_update: "YYYY-MM-DD"
  
  domains:
    economics:
      status: "active"
      aku_count: 1500
      subdomains:
        bwl:
          status: "active"
          aku_count: 58
          sme_agent: "sme-bwl-v1"
          quality_score: 0.95
          last_validation: "YYYY-MM-DD"
        
        vwl:
          status: "emerging"
          aku_count: 12
          sme_agent: "persona:economics-vwl"
          quality_score: 0.88
          note: "monitoring for specialist need"
    
    physics:
      status: "emerging"
      aku_count: 50
      subdomains:
        quantum:
          status: "detected"
          aku_count: 3
          sme_agent: null
          action: "monitor"
        
        classical:
          status: "detected"
          aku_count: 45
          sme_agent: "persona:physics-general"
          quality_score: 0.92

signals_for_coordinator:
  - "New domain detected: {domain_path}"
  - "Domain volume increasing: {domain_path} now has {count} AKUs"
  - "Cross-domain links emerging: {domain1} ↔ {domain2}"
```

### INVOKE: Coordinator Office
**TASK:** How to orchestrate SME agents for unknown domains?

**OUTPUT:**
```yaml
solution: "Dynamic Routing with Agent Registry"

agent_registry:
  structure:
    domain_path: "economics/bwl"
    handler_type: "specialist | persona | none"
    handler_id: "sme-bwl-v1 | persona:bwl-finance | null"
    status: "active | provisioning | retiring"
    metadata:
      created: "YYYY-MM-DD"
      last_used: "YYYY-MM-DD"
      usage_count: 1234

routing_logic:
  validation_request:
    input: "AKU to validate, domain_path"
    process:
      - "Query registry for domain_path"
      - "IF specialist exists AND active: route to specialist"
      - "ELIF persona exists: route to Generic Domain Empathy + persona"
      - "ELSE: route to Generic Domain Empathy + best-match persona"
    output: "Validation result"

  specialist_unavailable:
    - "Fallback to Generic Domain Empathy"
    - "Log: specialist needed but unavailable"
    - "Signal Recruiter: consider provisioning"

  load_balancing:
    - "IF multiple specialists for domain: round-robin"
    - "Track load per agent"
    - "Prevent single agent overload"

  escalation:
    - "IF validation fails repeatedly: escalate to human expert"
    - "IF no suitable agent exists: signal Recruiter"
    - "IF quality issues persist: signal QA Agent"

scalability:
  - "Coordinator Office is pool of coordinators (not single agent)"
  - "Can request additional coordinators as load increases"
  - "Stateless: any coordinator can handle any request"
```

### INVOKE: Quality Assurance Agent
**TASK:** How to monitor quality and trigger specialist provisioning?

**OUTPUT:**
```yaml
solution: "Quality-Based Triggers"

monitoring:
  by_domain:
    - "Track error rate per domain"
    - "Track correction rate per domain"
    - "Track user feedback per domain"
    - "Track peer review scores per domain"

thresholds:
  error_rate:
    warning: ">3%"
    critical: ">5%"
    action: "Signal Recruiter: provision specialist"
  
  correction_rate:
    warning: ">20%"
    critical: ">30%"
    action: "Persona inadequate, upgrade to specialist"
  
  user_feedback:
    warning: "<4.0/5.0 average"
    critical: "<3.5/5.0 average"
    action: "Investigate quality issues"

quality_audit_workflow:
  daily:
    - "Calculate error rates by domain"
    - "IF any domain exceeds threshold: alert"
  
  weekly:
    - "Generate quality report by domain"
    - "Rank domains by quality score"
    - "Bottom 10%: investigate"
  
  monthly:
    - "Deep dive: domains with persistent issues"
    - "Root cause analysis"
    - "Recommendation: specialist, better persona, or process change"

feedback_loop:
  - "Fact-checking finds errors → log by domain"
  - "Peer review scores AKU quality → log by domain"
  - "User reports issues → log by domain"
  - "Aggregate metrics → trend analysis"
  - "Trigger provisioning when thresholds exceeded"
```

### INVOKE: Contrarian Agent
**TASK:** Economic model for SME agent provisioning?

**OUTPUT:**
```yaml
solution: "Economic ROI Model"

cost_factors:
  specialist_agent:
    compute: "$X per month (dedicated resources)"
    maintenance: "$Y per month (updates, monitoring)"
    opportunity_cost: "Could those resources serve multiple domains?"
  
  generic_empathy_persona:
    compute: "$Z per validation (shared resources)"
    persona_updates: "$W per quarter"
    correction_overhead: "30% of validations need rework"

roi_calculation:
  specialist_justified_when:
    condition: "(specialist_cost < persona_cost_with_corrections) AND (volume > threshold)"
    volume_threshold: "1000 AKUs or 50 validations/month"
    quality_premium: "Specialist error rate <2% vs. persona 5-10%"
  
  break_even_analysis:
    - "Calculate: validations per month needed to justify specialist"
    - "Break-even point: ~50 validations/month for typical domain"
    - "Below break-even: persona more economical"
    - "Above break-even: specialist more economical"

pragmatic_recommendations:
  low_volume_domains:
    - "Use Generic Domain Empathy + persona"
    - "Accept slightly higher correction rate"
    - "Cost-effective for <100 AKUs or <10 validations/month"
  
  high_volume_domains:
    - "Provision specialist immediately if >1000 AKUs"
    - "Quality and efficiency gains justify cost"
  
  emerging_domains:
    - "Start with persona, monitor for 30 days"
    - "Provision specialist when volume or quality triggers hit"
  
  declining_domains:
    - "Retire specialist when usage <10 validations/month for 3 months"
    - "Preserve learning in persona library"
    - "Revert to Generic Domain Empathy + enhanced persona"

cost_audit:
  - "Track: actual cost per domain per month"
  - "Compare: specialist vs. persona costs"
  - "Identify: over-provisioned domains (specialist not needed)"
  - "Identify: under-provisioned domains (quality suffering)"
  - "Optimize: right-size agent infrastructure"
```

### INVOKE: Software Architecture Agent
**TASK:** Technical infrastructure for dynamic SME agents?

**OUTPUT:**
```yaml
solution: "Microservice Architecture for SME Agents"

architecture:
  sme_agent_as_microservice:
    - "Each SME agent = independent service"
    - "Can scale independently (horizontal)"
    - "Can deploy/undeploy without affecting others"
    - "Stateless: all state in knowledge graph"
  
  service_registry:
    - "Central registry of available SME agents"
    - "Service discovery: Coordinator queries registry"
    - "Health checks: monitor agent availability"
    - "Load balancing: route to available instances"
  
  hot_swap:
    - "Seamless transition: persona → specialist"
    - "No downtime: parallel operation during transition"
    - "Gradual cutover: validate specialist before full switch"
  
  persona_library:
    - "Personas as config files (YAML)"
    - "Version controlled (Git)"
    - "Hot-reload: update persona without restart"
    - "A/B testing: compare persona versions"

deployment_model:
  provisioning:
    - "Recruiter signals: need SME for domain X"
    - "Software Architecture: spin up microservice"
    - "Initialize with persona/knowledge sources"
    - "Register in service registry"
    - "Begin accepting validation requests"
  
  scaling:
    - "Monitor: requests per second"
    - "Auto-scale: add instances if load high"
    - "Auto-scale down: remove instances if load low"
  
  retirement:
    - "Recruiter signals: usage below threshold"
    - "Graceful shutdown: complete in-flight requests"
    - "Preserve logs and metrics"
    - "Update persona library with learnings"
    - "Deregister from service registry"

technical_stack:
  containerization: "Docker (isolation, portability)"
  orchestration: "Kubernetes (scaling, health checks)"
  service_mesh: "Istio (routing, observability)"
  configuration: "ConfigMaps (personas as config)"
  storage: "Git (knowledge graphs, personas)"
  monitoring: "Prometheus + Grafana (metrics, alerts)"
```

## Synthesized Framework

### Hybrid Model Consensus

**Vote Results:** 28/41 agents support hybrid model

**Models Considered:**
1. **Pure Generic (5 agents):** Only Generic Domain Empathy + unlimited personas
   - Pros: Simplest, most flexible
   - Cons: May lack depth, quality ceiling
   
2. **Hybrid (28 agents):** Start Generic, provision specialists as needed ✅
   - Pros: Best of both, economic, scalable
   - Cons: Complexity in provisioning logic
   
3. **Pre-Provision (8 agents):** Create specialists for major domains upfront
   - Pros: Immediate high quality
   - Cons: Wasteful for low-volume domains, can't predict all domains

**Winner: Hybrid Model**

### Detection System

**5 Trigger Rules for SME Specialist Provisioning:**

1. **Volume Threshold**
   ```
   IF domain_aku_count > 1000:
       provision_specialist()
   ```
   Rationale: High volume justifies dedicated resource

2. **Quality Threshold**
   ```
   IF domain_error_rate > 5%:
       provision_specialist()
   ```
   Rationale: Persona inadequate for quality requirements

3. **Efficiency Threshold**
   ```
   IF domain_validation_time > 2 * average_time:
       investigate_need()
   ```
   Rationale: Persona causing inefficiency

4. **Persona Inadequacy**
   ```
   IF persona_correction_rate > 30%:
       provision_specialist()
   ```
   Rationale: Too many corrections needed

5. **User Demand**
   ```
   IF user_requests_for_domain > 3:
       provision_specialist()
   ```
   Rationale: Explicit need expressed

### Provisioning Process

```
Step 1: Detection
├─ Meta-Learning monitors metrics
├─ QA monitors quality
├─ Research discovers domains
└─ Triggers evaluated

Step 2: Decision
├─ IF trigger fires: signal Recruiter
├─ Recruiter checks registry
│   ├─ Specialist exists? Route to it
│   ├─ Persona adequate? Use Generic Domain Empathy
│   └─ Otherwise: Provision specialist
└─ Economic model validates decision

Step 3: Provisioning
├─ Recruiter creates SME agent from template
├─ Software Architecture deploys microservice
├─ Initialize with knowledge sources
├─ Register in service registry
└─ Coordinator begins routing

Step 4: Monitoring
├─ Meta-Learning tracks performance
├─ QA monitors quality
├─ Contrarian monitors costs
└─ Feedback loop for continuous improvement

Step 5: Retirement (when usage drops)
├─ Recruiter detects low usage (<10/month)
├─ Analyze: temporary dip or permanent decline?
├─ If permanent: decommission specialist
├─ Update persona library with learnings
└─ Revert to Generic Domain Empathy
```

### Lifecycle Management

**Stage 1: Discovery**
- Domain detected from content
- Research Agent updates taxonomy
- Initial routing to Generic Domain Empathy + persona

**Stage 2: Persona Phase (Default)**
- Generic Domain Empathy handles all validation
- Meta-Learning monitors for 100 AKUs or 30 days
- Quality and efficiency metrics tracked

**Stage 3: Evaluation**
- After monitoring period, evaluate metrics
- Decision matrix:
  ```
  IF (error_rate >5%) OR (correction_rate >30%) OR (volume >1000):
      → Provision specialist
  ELSE:
      → Continue with persona
  ```

**Stage 4: Specialist Phase**
- Dedicated SME agent deployed
- High-quality, efficient validation
- Continuous monitoring

**Stage 5: Retirement**
- Usage drops below threshold
- Decommission specialist
- Preserve knowledge in persona library
- Revert to persona

### Audit Framework

**Conducted by Recruiter Agent (Monthly)**

**1. Coverage Audit**
```yaml
objective: "Ensure all active domains have adequate support"

analysis:
  - "List all active domains (>10 AKUs)"
  - "Check: specialist OR persona available?"
  - "Identify gaps: domains without support"
  - "Prioritize: by volume and quality needs"

output:
  gaps: ["domain1 (no persona)", "domain2 (persona inadequate)"]
  actions: ["Create persona for domain1", "Provision specialist for domain2"]
```

**2. Performance Audit**
```yaml
objective: "Ensure agents meeting performance targets"

metrics_per_agent:
  - "Error rate (target: <2% for specialists, <5% for personas)"
  - "Response time (target: <5 min)"
  - "Throughput (target: >20 AKUs/day)"
  - "Utilization (target: 50-80%)"

analysis:
  - "Rank agents by performance"
  - "Identify underperformers"
  - "Identify overutilized (need scaling)"
  - "Identify underutilized (candidates for retirement)"

output:
  underperformers: ["sme-physics-v1 (8% error rate)"]
  overutilized: ["sme-bwl-v1 (95% utilization)"]
  underutilized: ["sme-chemistry-v2 (5% utilization)"]
  actions: 
    - "Retrain physics specialist"
    - "Scale BWL specialist"
    - "Consider retiring chemistry specialist"
```

**3. Economic Audit**
```yaml
objective: "Ensure cost-effective agent infrastructure"

costs_per_domain:
  - "Compute costs (specialist vs. persona)"
  - "Human review costs (corrections, escalations)"
  - "Total cost of ownership"

roi_analysis:
  - "Cost per validated AKU"
  - "Compare: specialist vs. persona"
  - "Identify: over-provisioned (specialist not justified)"
  - "Identify: under-provisioned (quality suffering, rework expensive)"

output:
  over_provisioned: ["chemistry (only 5 validations/month, specialist costs $X)"]
  under_provisioned: ["biology (persona costs $Y in corrections, specialist would cost $Z)"]
  actions:
    - "Retire chemistry specialist"
    - "Provision biology specialist"
```

**4. Evolution Audit**
```yaml
objective: "Track domain landscape changes"

trends:
  growing_domains:
    - "Identify: domains with increasing AKU counts"
    - "Predict: when will they need specialists?"
    - "Proactive: provision before quality issues arise"
  
  declining_domains:
    - "Identify: domains with decreasing activity"
    - "Predict: when to retire specialists?"
    - "Preserve: knowledge before retirement"
  
  emerging_domains:
    - "Identify: new domains being added"
    - "Assess: initial persona requirements"
    - "Monitor: for growth patterns"
  
  cross_domain_patterns:
    - "Identify: domains frequently linked"
    - "Consider: integrated specialist (e.g., biochemistry)"

output:
  growing: ["machine learning (+200 AKUs/month)"]
  declining: ["classical literature (-50 AKUs/month)"]
  emerging: ["bioinformatics (new, 15 AKUs)"]
  cross_domain: ["physics ↔ mathematics (high overlap)"]
  actions:
    - "Prepare ML specialist for Q2"
    - "Monitor classical lit for retirement"
    - "Create bioinformatics persona"
    - "Consider physics-math integrated specialist"
```

## Practical Workflows

### Workflow 1: New Domain Emerges

**Scenario:** Users start adding Quantum Physics content

```
Day 1: First 3 AKUs added
├─ Content added to domain/physics/quantum/
├─ Research Agent detects new domain
├─ Updates domain taxonomy
├─ Coordinator checks registry: no SME, no persona
├─ Routes to Generic Domain Empathy
├─ Generic loads "physics-general" persona (best match)
└─ Validates 3 AKUs (success rate: 95%)

Week 2: 50 AKUs added
├─ Generic Domain Empathy + persona handling all
├─ Meta-Learning tracks metrics:
│   ├─ Success rate: 85%
│   ├─ Correction rate: 15%
│   ├─ Error rate: 3%
│   └─ Validation time: 1.2x average
├─ All below thresholds
└─ Continue with persona

Month 2: 500 AKUs added, heavy validation load
├─ Meta-Learning notices degradation:
│   ├─ Success rate: 70% (dropped)
│   ├─ Correction rate: 32% (above 30% threshold)
│   ├─ Error rate: 8% (above 5% threshold)
│   ├─ Validation time: 3x average (above 2x threshold)
│   └─ Volume: 500 AKUs (approaching 1000 threshold)
├─ Detection engine fires: "provision specialist"
├─ Signal sent to Recruiter
└─ Recruiter evaluates: confirmed, provision

Month 2 + 1 day: Specialist provisioned
├─ Recruiter creates "SME-Quantum-Physics-v1"
├─ Software Architecture deploys microservice
├─ Initialize with knowledge sources:
│   ├─ Textbooks: "Griffiths Quantum Mechanics", "Sakurai"
│   ├─ Papers: 50 foundational papers
│   └─ Human expert: prof.quantum@university.edu
├─ Register in service registry
├─ Coordinator begins routing quantum validation to specialist
├─ Generic Domain Empathy no longer handles quantum
└─ Persona preserved for light queries

Month 3-7: Specialist operating
├─ Meta-Learning tracks performance:
│   ├─ Error rate: 1.5% (excellent)
│   ├─ Correction rate: 8% (good)
│   ├─ Validation time: 0.8x average (efficient)
│   └─ Throughput: 25 AKUs/day
├─ Quality improved significantly
└─ Users satisfied

Month 8: Activity drops
├─ Quantum content stabilized
├─ Only 5 validations per month (below 10 threshold)
├─ Recruiter detects low utilization
├─ Economic audit: specialist costs $X, low ROI
├─ Decision: retire specialist
└─ Retirement process initiated

Month 8 + 7 days: Retirement complete
├─ Specialist completes final validations
├─ Learnings extracted and analyzed
├─ "physics-quantum" persona updated with specialist knowledge:
│   ├─ Common errors to watch for
│   ├─ Key formulas and their derivations
│   ├─ Reference standards
│   └─ Quality guidelines
├─ Specialist decommissioned
├─ Service deregistered
└─ Coordinator reverts quantum validation to Generic Domain Empathy + enhanced persona
```

### Workflow 2: Quality Issues Detected

**Scenario:** Biology domain has persistent quality issues

```
Week 1-4: Normal operations
├─ Biology using Generic Domain Empathy + "biology-general" persona
├─ Validation proceeding
└─ No issues

Week 5: QA Agent detects pattern
├─ Fact-checking finds errors in 3 biology AKUs
├─ Error rate for biology: 6% (above 5% threshold)
├─ QA Agent logs: biology domain quality issue
└─ Alert sent to Recruiter

Week 5 + 1 day: Investigation
├─ Recruiter requests detailed analysis from QA
├─ QA analyzes errors:
│   ├─ 2 errors: outdated research (2019 textbook, 2023 research supersedes)
│   ├─ 1 error: misunderstanding of complex mechanism
│   └─ Root cause: persona based on older knowledge
├─ Recruiter evaluates options:
│   ├─ Option A: Update persona with latest research
│   ├─ Option B: Provision specialist
│   └─ Decision matrix: volume = 200 AKUs, not yet at 1000 threshold
├─ Decision: Update persona first, monitor
└─ If errors persist: provision specialist

Week 6: Persona updated
├─ Recruiter updates "biology-general" persona
├─ Adds 2023 research papers
├─ Adds clarification on complex mechanisms
├─ Version bump: v1.2 → v1.3
└─ Generic Domain Empathy loads updated persona

Week 7-10: Monitoring
├─ Meta-Learning tracks biology validation
├─ Error rate: 2% (below threshold)
├─ Correction rate: 12% (acceptable)
├─ Problem resolved without specialist
└─ Continued monitoring

Alternative: If errors persisted
├─ Week 7: Still 6% error rate
├─ QA signals: persona update insufficient
├─ Recruiter decision: provision specialist
└─ Specialist handles biology validation going forward
```

### Workflow 3: Economic Optimization

**Scenario:** Monthly economic audit reveals over-provisioning

```
Month 1: Economic audit run
├─ Contrarian Agent analyzes costs per domain
├─ Chemistry specialist identified:
│   ├─ Cost: $500/month
│   ├─ Usage: 5 validations/month
│   ├─ Cost per validation: $100
│   └─ Persona cost per validation (with corrections): $15
├─ Analysis: Over-provisioned
│   ├─ Specialist cost: $500/month
│   ├─ Persona cost: 5 validations × $15 = $75/month
│   ├─ Savings if retired: $425/month
│   └─ Quality acceptable with persona (error rate 4%)
├─ Recommendation: Retire chemistry specialist
└─ Report to Coordinator

Month 1 + 3 days: Decision
├─ Coordinator reviews recommendation
├─ Confirms: usage has been <10/month for 3 months
├─ Confirms: quality acceptable with persona
├─ Decision: Approved, retire specialist
└─ Retirement process initiated

Month 1 + 7 days: Retirement
├─ Chemistry specialist completes final validations
├─ Learnings extracted:
│   ├─ Common chemistry validation patterns
│   ├─ Frequently used formulas
│   ├─ Quality standards specific to chemistry
│   └─ Reference materials
├─ "chemistry-general" persona updated to v2.0
├─ Specialist decommissioned
├─ Coordinator routes chemistry to Generic Domain Empathy + persona
└─ Cost savings: $425/month achieved

Month 2-4: Monitoring
├─ Meta-Learning tracks chemistry validation
├─ Error rate: 4% (acceptable, below 5%)
├─ Correction rate: 18% (acceptable)
├─ Cost: $15/validation, ~$75/month
├─ Quality maintained, cost reduced
└─ Economic optimization successful

Trigger for re-provisioning (if needed):
├─ IF activity increases (>50 validations/month)
├─ OR error rate climbs (>5%)
├─ OR volume grows (>1000 AKUs)
└─ THEN: Re-provision chemistry specialist
```

## Implementation Checklist

### Phase 1: Foundation (Months 1-2)
- [ ] Implement domain taxonomy auto-discovery (Research Agent)
- [ ] Implement metrics tracking system (Meta-Learning Agent)
- [ ] Implement detection rules engine (Meta-Learning Agent)
- [ ] Implement SME agent registry (Coordinator Office)
- [ ] Implement agent provisioning templates (Recruiter Agent)
- [ ] Create 10 baseline personas (major domains)
- [ ] Deploy Generic Domain Empathy Agent
- [ ] Test: provision one specialist manually, validate lifecycle

### Phase 2: Automation (Months 3-4)
- [ ] Automate detection triggers
- [ ] Automate specialist provisioning
- [ ] Automate routing to specialists vs. personas
- [ ] Implement quality monitoring (QA Agent)
- [ ] Implement economic monitoring (Contrarian Agent)
- [ ] Test: auto-provision specialist when trigger fires

### Phase 3: Optimization (Months 5-6)
- [ ] Implement monthly audit framework (Recruiter Agent)
- [ ] Implement auto-retirement for idle specialists
- [ ] Implement persona learning from specialists
- [ ] Implement A/B testing for persona vs. specialist
- [ ] Refine detection thresholds based on data
- [ ] Test: full lifecycle (provision → operate → retire)

### Phase 4: Scaling (Months 7-12)
- [ ] Deploy to production
- [ ] Monitor across multiple domains simultaneously
- [ ] Refine economic model based on real costs
- [ ] Expand persona library to 50+ domains
- [ ] Implement advanced features (cross-domain specialists, etc.)
- [ ] Validate: system handles unknown domains gracefully

## Success Metrics

### Coverage Metrics
- **Domain Coverage:** % of active domains with adequate SME support
  - Target: 100% of domains with >100 AKUs
- **Persona Library:** Number of personas available
  - Target: 50+ personas by end of year 1

### Quality Metrics
- **Error Rate:** % of validated AKUs with errors (by domain)
  - Target: <5% for persona, <2% for specialist
- **Correction Rate:** % of validations needing corrections
  - Target: <30% for persona, <10% for specialist
- **User Satisfaction:** Feedback scores (1-5)
  - Target: >4.0 average

### Efficiency Metrics
- **Validation Time:** Average time to validate per AKU
  - Target: <5 minutes
- **Throughput:** AKUs validated per day (per agent)
  - Target: >20 AKUs/day for specialist, >10 for persona
- **Utilization:** % of time agents are actively working
  - Target: 50-80% (not underutilized, not overloaded)

### Economic Metrics
- **Cost per Domain:** Monthly cost to support each domain
  - Target: Minimize while maintaining quality
- **ROI:** Value delivered vs. cost
  - Target: Specialist justified when volume >1000 AKUs
- **Cost per AKU:** Total cost / total AKUs validated
  - Target: <$1 per AKU validated

### Adaptive Metrics
- **Detection Accuracy:** % of correct specialist provisioning decisions
  - Target: >90% (few false positives or false negatives)
- **Time to Provision:** Time from detection to specialist operational
  - Target: <24 hours
- **Time to Retire:** Time from low utilization to retirement
  - Target: <7 days

## Conclusion

**Key Achievement:** Solved the "unknown domains" problem with a domain-agnostic infrastructure that:

1. **Adapts:** Automatically discovers new domains from content
2. **Detects:** Recognizes when Generic Domain Empathy + persona is insufficient
3. **Provisions:** Dynamically creates specialists when justified
4. **Optimizes:** Right-sizes infrastructure based on volume, quality, and economics
5. **Retires:** Decommissions underutilized specialists, preserving knowledge
6. **Learns:** Continuously improves detection rules and personas

**Agent Consensus:** 28/41 agents support this hybrid model

**No New Permanent Agents:** Framework uses existing 41 agents with new workflows

**Dynamic SME Agents:** Created and destroyed as needed, not counted in base 41

**Ready for:** Unknown domains (Physics, Law, Medicine, etc.) - system will adapt automatically
