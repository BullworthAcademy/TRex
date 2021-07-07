# !/bin/bash
# Bash script for loading the rule files corresponding to rule 1

for ((i = 0; i < 1000; i++)); do
        java -jar TRex-client.jar localhost 50254 -rule "trex_rules/trex1_$i.rule"
done
