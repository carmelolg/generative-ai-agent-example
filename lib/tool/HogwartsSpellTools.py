"""
SpellFunctions module for retrieving Harry Potter spell information.
"""
from lib.service import HogwartsHttpService, KnowledgeService


def available_functions() -> dict:
    """
    Returns a dictionary of available functions for spell information retrieval.
    :return: dictionary of functions
    """
    return {
        "get_spell_use": get_spell_use,
        "get_spell_name": get_spell_name
    }

def get_spell_use(spell: str) -> dict:
    """
    Get the use of a Harry Potter spell
    Args:
      spell: The name of the spell
    Returns:
        The use of the spell and the similarity score
    """
    spells = HogwartsHttpService.get_spells()

    if spells is None or len(spells) == 0:
        return {'result': "Not found", 'similarity': 0.0}

    spell_db = KnowledgeService.build_knowledge(list(map(_map_spell, spells)))

    most_relevant_spells = KnowledgeService.get_most_relevant_chunks(spell.lower(), spell_db, top_n=1)
    for spell in spells:
        if most_relevant_spells[0][0] == spell['spell'].lower():
            return {'use': spell['use'], 'similarity': most_relevant_spells[0][1]}
    return {'result': "Not found", 'similarity': 0.0}


def get_spell_name(use: str) -> dict:
    """
    Get the name of a Harry Potter spell based on its use
    Args:
      use: The use of the spell
    Returns:
        The name of the spell and the similarity score
    """
    spells = HogwartsHttpService.get_spells()

    if spells is None or len(spells) == 0:
        return {'result': "Not found", 'similarity': 0.0}

    use_db = KnowledgeService.build_knowledge(list(map(_map_use, spells)))

    most_relevant_use = KnowledgeService.get_most_relevant_chunks(use.lower(), use_db, top_n=1)

    for use in spells:
        if most_relevant_use[0][0] == use['use'].lower():
            return {'spell': use['spell'], 'similarity': most_relevant_use[0][1]}
    return {'result': "Not found", 'similarity': 0.0}


def _map_spell(spell):
    return spell['spell'].lower()


def _map_use(spell):
    return spell['use'].lower()

