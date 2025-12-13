import requests
from lib import KnowledgeService, HttpService


def map_spell(spell):
    return spell['spell'].lower()

def map_use(spell):
    return spell['use'].lower()


def get_spell_use(spell: str) -> str:
    """
    Get the use of a Harry Potter spell
    Args:
      spell: The name of the spell
    Returns:
        The use of the spell
    """
    spells = HttpService.get("spells", "en")
    spell_db = KnowledgeService.build_knowledge(list(map(map_spell, spells)))

    most_relevant_spells = KnowledgeService.get_most_relevant_chunks(spell.lower(), spell_db, top_n=1)

    for spell in spells:
        if most_relevant_spells[0][0] == spell['spell'].lower():
            return spell['use']

    return "Not found"

def get_spell_name(use: str) -> str:
    """
    Get the name of a Harry Potter spell based on its use
    Args:
      use: The use of the spell
    Returns:
        The name of the spell
    """
    spells = HttpService.get("spells", "en")
    use_db = KnowledgeService.build_knowledge(list(map(map_use, spells)))

    most_relevant_use = KnowledgeService.get_most_relevant_chunks(use.lower(), use_db, top_n=1)

    for use in spells:
        if most_relevant_use[0][0] == use['use'].lower():
            return use['spell']

    return "Not found"
