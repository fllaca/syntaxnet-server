## Based on specs here: http://universaldependencies.org/format.html

from universal_dependencies import *
from lemmatizer import lemmatize


def conll2tree(conll):
    """
    Converts a conll table in a syntax tree
    """
    # Get node list
    nodelist = buildNodeList(conll)
        
    # Build tree
    root = None
    for node in nodelist:
        if node['head'] == 0:
            root = node
        else:
            head = node['head']
            nodelist[head - 1]['children'].append(node)

    return root

def buildFeatList(feats):
    feat_pairs = feats.split("|")
    result = {}
    for feat_pair in feat_pairs:
        tokens=feat_pair.split("=")
        result[tokens[0]] = tokens[1]
    return result

def buildNodeList(conll):
    # Get node list
    nodelist = []
    for conll_entry in conll:
        nodelist.append({
            'id': int(conll_entry[ID_INDEX]),
            'head': int(conll_entry[HEAD_INDEX]),
            'form': conll_entry[FORM_INDEX],
            'upostag': conll_entry[UPOSTAG_INDEX],
            'xpostag': conll_entry[XPOSTAG_INDEX],
            'feats': buildFeatList(conll_entry[FEATS_INDEX]),
            # NOT USED: 'deprel': int(conll_entry[DEPREL_INDEX]),
            'deps': conll_entry[DEPS_INDEX],
            'lemma': lemmatize(conll_entry[FORM_INDEX], conll_entry[UPOSTAG_INDEX]),
            'children': []
        })
    return nodelist
