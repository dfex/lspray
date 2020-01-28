#!/usr/bin/env python3

# lspray - The LSP spray can
#
# Quick and dirty full-mesh LSP configuration generator for Junos
#
# ben.dale@gmail.com
# 28/01/2020

pe_routers = {
    'pe1-syd':'10.255.255.1',
    'pe2-syd':'10.255.255.2',
    'pe1-bne':'10.255.255.3',
    'pe2-bne':'10.255.255.4',
    'pe1-per':'10.255.255.5',
    'pe2-per':'10.255.255.6',
    'pe1-cnb':'10.255.255.7',
    'pe2-cnb':'10.255.255.8',
    'pe1-mel':'10.255.255.9',
    'pe2-mel':'10.255.255.10',
    'pe1-adl':'10.255.255.11',
    'pe2-adl':'10.255.255.12',
    'pe1-ben':'10.255.255.13',
    'pe2-ben':'10.255.255.14',
    'pe1-gym':'10.255.255.15',
    'pe2-gym':'10.255.255.16',
    'pe1-crn':'10.255.255.17',
    'pe2-crn':'10.255.255.18',
    'pe1-tvl':'10.255.255.19',
    'pe2-tvl':'10.255.255.20',
}

for ingress_node in pe_routers.keys():
    print ("\n### " + ingress_node + " configuration:")
    for egress_node, egress_ip in pe_routers.items():
        if egress_node == ingress_node:
            continue
        else:
            print ("set protocols mpls label-switched-path " + ingress_node + "->" + egress_node + " to " + egress_ip)
            print ("set protocols mpls label-switched-path " + ingress_node + "->" + egress_node + " primary <<primary-path>>")
            print ("set protocols mpls label-switched-path " + ingress_node + "->" + egress_node + " secondary <<secondary-path>>")
            # you can put your other LSP attributes in here, but apply-groups are a better way of doing this


