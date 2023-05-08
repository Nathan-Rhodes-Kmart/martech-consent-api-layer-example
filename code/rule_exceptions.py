def PI_EM_RuleExceptions(hierarchy, incomingConsent, currentConsent, currentConsentState, newState):
    #Whittle Rule Exceptions
    #Add additional if conditions here for each source that causes an exception to the basic hierarchy
    if incomingConsent.name == 'whittle':
        Hierarchy_values = []
        for key, value in hierarchy.items():
            for x in value:
                if(x.name == 'whittle'):
                    Hierarchy_values.append(key)
        #Whittle True
        if(newState == 'Inferred Yes'):
            hierarchy[Hierarchy_values[1]].remove(incomingConsent)
        #Whittle False
        if newState == 'Soft No':
            hierarchy[Hierarchy_values[0]].remove(incomingConsent)
            #Current source is Whittle
            if currentConsent.name == 'whittle':
                return [1, {
                    'source': 'whittle',
                    'state':  'Soft No'
                }]
    elif currentConsent.name == 'whittle':
        Hierarchy_values = []
        for key, value in hierarchy.items():
            for x in value:
                if(x.name == 'whittle'):
                    Hierarchy_values.append(key)
        #Whittle True
        if(currentConsentState == 'Inferred Yes'):
            hierarchy[Hierarchy_values[1]].remove(currentConsent)
        #Whittle False
        if currentConsentState == 'Soft No':
            hierarchy[Hierarchy_values[0]].remove(currentConsent)

    return [0, hierarchy]

def PI_TA_RuleExceptions(hierarchy, incomingConsent, currentConsent, currentConsentState, newState):
    if incomingConsent.name == 'whittle':
        Hierarchy_values = []
        for key, value in hierarchy.items():
            for x in value:
                if(x.name == 'whittle'):
                    Hierarchy_values.append(key)
        #Whittle True
        if(newState == 'Inferred Yes'):
            hierarchy[Hierarchy_values[1]].remove(incomingConsent)
        #Whittle False
        if newState == 'Soft No':
            hierarchy[Hierarchy_values[0]].remove(incomingConsent)
            #Current source is Whittle
            if currentConsent.name == 'whittle':
                return [1, {
                    'source': 'whittle',
                    'state':  'Soft No'
                }]
    elif currentConsent.name == 'whittle':
        Hierarchy_values = []
        for key, value in hierarchy.items():
            for x in value:
                if(x.name == 'whittle'):
                    Hierarchy_values.append(key)
        #Whittle True
        if(currentConsentState == 'Inferred Yes'):
            hierarchy[Hierarchy_values[1]].remove(currentConsent)
        #Whittle False
        if currentConsentState == 'Soft No':
            hierarchy[Hierarchy_values[0]].remove(currentConsent)
    return [0, hierarchy]
