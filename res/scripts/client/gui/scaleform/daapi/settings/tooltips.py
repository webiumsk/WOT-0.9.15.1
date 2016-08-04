# 2016.08.04 19:49:36 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/settings/tooltips.py
from gui.shared.tooltips import vehicle, tankman, skill, shell, module, achievement, cybersport, common, contexts, potapovquests, tutorial, fortifications, clans, boosters
from gui.Scaleform.daapi.view.lobby.customization.tooltips import BonusTooltip as CustomizationBonusTooltip
from gui.Scaleform.daapi.view.lobby.customization.tooltips import ElementTooltip as CustomizationElementTooltip, QuestElementTooltip as CustomizationQuestElementTooltip
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips.filter import VehicleFilterTooltip
TOOLTIPS = {TOOLTIPS_CONSTANTS.TANKMAN: {'tooltip': TOOLTIPS_CONSTANTS.TANKMEN_UI,
                              'method': lambda invID, isCurrentVehicle = None: tankman.TankmanTooltipData(contexts.TankmanHangarContext()).buildToolTip(invID),
                              'complex': None},
 TOOLTIPS_CONSTANTS.TANKMAN_SKILL: {'tooltip': TOOLTIPS_CONSTANTS.TANKMEN_SKILL_UI,
                                    'method': skill.SkillTooltipData(contexts.PersonalCaseContext(fieldsToExclude=('count',))).buildToolTip,
                                    'complex': None},
 TOOLTIPS_CONSTANTS.TANKMAN_NEW_SKILL: {'tooltip': TOOLTIPS_CONSTANTS.TANKMEN_BUY_SKILL_UI,
                                        'method': skill.BuySkillTooltipData(contexts.NewSkillContext()).buildToolTip,
                                        'complex': lambda tooltipData: tooltipData['count'] > 1 or tooltipData['level'] > 0},
 TOOLTIPS_CONSTANTS.BATTLE_STATS_ACHIEVS: {'tooltip': TOOLTIPS_CONSTANTS.ACHIEVEMENT_UI,
                                           'method': achievement.AchievementTooltipData(contexts.BattleResultContext()).buildToolTip,
                                           'complex': None},
 TOOLTIPS_CONSTANTS.ACHIEVEMENT: {'tooltip': TOOLTIPS_CONSTANTS.ACHIEVEMENT_UI,
                                  'method': achievement.AchievementTooltipData(contexts.ProfileContext()).buildToolTip,
                                  'complex': None},
 TOOLTIPS_CONSTANTS.MARKS_ON_GUN_ACHIEVEMENT: {'tooltip': TOOLTIPS_CONSTANTS.MARKS_ON_GUN_UI,
                                               'method': achievement.AchievementTooltipData(contexts.ProfileContext()).buildToolTip,
                                               'complex': None},
 TOOLTIPS_CONSTANTS.BATTLE_STATS_MARKS_ON_GUN_ACHIEVEMENT: {'tooltip': TOOLTIPS_CONSTANTS.MARKS_ON_GUN_UI,
                                                            'method': achievement.AchievementTooltipData(contexts.BattleResultMarksOnGunContext()).buildToolTip,
                                                            'complex': None},
 TOOLTIPS_CONSTANTS.GLOBAL_RATING: {'tooltip': TOOLTIPS_CONSTANTS.ACHIEVEMENT_UI,
                                    'method': achievement.GlobalRatingTooltipData(contexts.ProfileContext()).buildToolTip,
                                    'complex': None},
 'achievementAttr': {'tooltip': TOOLTIPS_CONSTANTS.ACHIEVEMENT_UI,
                     'method': None,
                     'complex': None},
 TOOLTIPS_CONSTANTS.MARK_OF_MASTERY: {'tooltip': TOOLTIPS_CONSTANTS.MARK_OF_MASTERY_UI,
                                      'method': achievement.AchievementTooltipData(contexts.BattleResultMarkOfMasteryContext()).buildToolTip,
                                      'complex': None},
 TOOLTIPS_CONSTANTS.CAROUSEL_VEHICLE: {'tooltip': TOOLTIPS_CONSTANTS.VEHICLE_INFO_UI,
                                       'method': vehicle.VehicleInfoTooltipData(contexts.CarouselContext()).buildToolTip,
                                       'complex': None},
 TOOLTIPS_CONSTANTS.INVENTORY_VEHICLE: {'tooltip': TOOLTIPS_CONSTANTS.VEHICLE_INFO_UI,
                                        'method': lambda intCD, sellPrice = 0, sellCurrency = 0, inventoryCount = 0, vehicleCount = 0: vehicle.VehicleInfoTooltipData(contexts.InventoryContext()).buildToolTip(intCD),
                                        'complex': None},
 TOOLTIPS_CONSTANTS.TECHTREE_VEHICLE: {'tooltip': TOOLTIPS_CONSTANTS.VEHICLE_INFO_UI,
                                       'method': vehicle.VehicleInfoTooltipData(contexts.TechTreeContext()).buildToolTip,
                                       'complex': None},
 TOOLTIPS_CONSTANTS.SHOP_VEHICLE: {'tooltip': TOOLTIPS_CONSTANTS.VEHICLE_INFO_UI,
                                   'method': lambda intCD, inventoryCount = 0, vehicleCount = 0: vehicle.VehicleInfoTooltipData(contexts.ShopContext()).buildToolTip(intCD),
                                   'complex': None},
 TOOLTIPS_CONSTANTS.INVENTORY_MODULE: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                       'method': lambda intCD, sellPrice = 0, sellCurrency = 0, inventoryCount = 0, vehicleCount = 0: module.ModuleBlockTooltipData(contexts.InventoryContext()).buildToolTip(intCD),
                                       'complex': None},
 TOOLTIPS_CONSTANTS.TECH_MAIN_MODULE: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                       'method': lambda intCD, buyPrice = None, inventoryCount = 0, vehicleCount = 0, slotIdx = 0, eqs = None: module.ModuleBlockTooltipData(contexts.TechMainContext()).buildToolTip(intCD, slotIdx, eqs),
                                       'complex': None},
 TOOLTIPS_CONSTANTS.HANGAR_MODULE: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                    'method': module.ModuleBlockTooltipData(contexts.HangarContext()).buildToolTip,
                                    'complex': None},
 TOOLTIPS_CONSTANTS.PREVIEW_MODULE: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                     'method': module.ModuleBlockTooltipData(contexts.PreviewContext()).buildToolTip,
                                     'complex': None},
 TOOLTIPS_CONSTANTS.TECHTREE_MODULE: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                      'method': module.ModuleBlockTooltipData(contexts.TechTreeContext()).buildToolTip,
                                      'complex': None},
 TOOLTIPS_CONSTANTS.SHOP_MODULE: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                  'method': lambda intCD, inventoryCount = 0, vehicleCount = 0: module.ModuleBlockTooltipData(contexts.ShopContext()).buildToolTip(intCD),
                                  'complex': None},
 TOOLTIPS_CONSTANTS.SHOP_SHELL: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                 'method': lambda intCD, inventoryCount = 0, vehicleCount = 0: shell.ShellBlockToolTipData(contexts.ShopContext()).buildToolTip(intCD),
                                 'complex': None},
 TOOLTIPS_CONSTANTS.HANGAR_SHELL: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                   'method': lambda intCD, historicalBattleID = -1: shell.ShellBlockToolTipData(contexts.HangarContext()).buildToolTip(intCD, historicalBattleID=historicalBattleID),
                                   'complex': None},
 TOOLTIPS_CONSTANTS.INVENTORY_SHELL: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                      'method': lambda intCD, sellPrice = 0, sellCurrency = 0, inventoryCount = 0, vehicleCount = 0: shell.ShellBlockToolTipData(contexts.InventoryContext()).buildToolTip(intCD),
                                      'complex': None},
 TOOLTIPS_CONSTANTS.TECH_MAIN_SHELL: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                      'method': lambda intCD, buyPrice = None, inventoryCount = 0, vehicleCount = 0, slotIdx = 0, eqs = None: shell.ShellBlockToolTipData(contexts.TechMainContext()).buildToolTip(intCD, slotIdx, eqs),
                                      'complex': None},
 TOOLTIPS_CONSTANTS.EFFICIENCY_PARAM: {'tooltip': TOOLTIPS_CONSTANTS.FINAL_STSTS_UI,
                                       'method': common.EfficiencyTooltipData(contexts.FinalStatisticContext()).buildToolTip,
                                       'complex': None},
 TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_RESEARCH_VEHICLE_INFO: {'tooltip': TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_RESEARCH_VEHICLE_INFO_UI,
                                                            'method': tutorial.ResearchVehicleInfoPacker(contexts.HangarTutorialContext()).buildToolTip,
                                                            'complex': None},
 TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_RESEARCH_MODULES_PREMIUM: {'tooltip': TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_RESEARCH_MODULES_PREMIUM_UI,
                                                               'method': tutorial.ResearchModulesPacker(contexts.HangarTutorialContext()).buildToolTip,
                                                               'complex': None},
 TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_RESEARCH_MODULES: {'tooltip': TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_RESEARCH_MODULES_UI,
                                                       'method': tutorial.ResearchModulesPackerEx(contexts.HangarTutorialContext()).buildToolTip,
                                                       'complex': None},
 TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_CUSTOMIZATION_TYPES: {'tooltip': TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_CUSTOMIZATION_TYPES_UI,
                                                          'method': tutorial.CustomizationTypesPacker(contexts.HangarTutorialContext()).buildToolTip,
                                                          'complex': None},
 TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_NATIONS: {'tooltip': TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_NATIONS_UI,
                                              'method': tutorial.NationsPacker(contexts.HangarTutorialContext()).buildToolTip,
                                              'complex': None},
 TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_RESEARCH_TREE: {'tooltip': TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_RESEARCH_TREE_UI,
                                                    'method': tutorial.ResearchTreePacker(contexts.HangarTutorialContext()).buildToolTip,
                                                    'complex': None},
 TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_PERSONAL_CASE_SKILLS: {'tooltip': TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_PERSONAL_CASE_SKILLS_UI,
                                                           'method': tutorial.PersonalCaseSkillsPacker(contexts.HangarTutorialContext()).buildToolTip,
                                                           'complex': None},
 TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_PERSONAL_CASE_PERKS: {'tooltip': TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_PERSONAL_CASE_PERKS_UI,
                                                          'method': tutorial.PersonalCasePerksPacker(contexts.HangarTutorialContext()).buildToolTip,
                                                          'complex': None},
 TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_PERSONAL_CASE_ADDITIONAL: {'tooltip': TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_PERSONAL_CASE_ADDITIONAL_UI,
                                                               'method': tutorial.PersonalCaseAdditionalPacker(contexts.HangarTutorialContext()).buildToolTip,
                                                               'complex': None},
 TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_AMMUNITION: {'tooltip': TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_AMMUNITION_UI,
                                                 'method': tutorial.AmmunitionPacker(contexts.HangarTutorialContext()).buildToolTip,
                                                 'complex': None},
 TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_EQUPMENT: {'tooltip': TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_EQUPMENT_UI,
                                               'method': tutorial.EquipmentPacker(contexts.HangarTutorialContext()).buildToolTip,
                                               'complex': None},
 TOOLTIPS_CONSTANTS.IGR_INFO: {'tooltip': TOOLTIPS_CONSTANTS.IGR_INFO_UI,
                               'method': common.IgrTooltipData(contexts.HangarContext()).buildToolTip,
                               'complex': None},
 TOOLTIPS_CONSTANTS.CYBER_SPORT_SLOT: {'tooltip': TOOLTIPS_CONSTANTS.SUITABLE_VEHICLE_UI,
                                       'method': cybersport.CybersportSlotToolTipData(contexts.CyberSportUnitContext()).buildToolTip,
                                       'complex': None},
 TOOLTIPS_CONSTANTS.CYBER_SPORT_SELECTED_VEHICLE: {'tooltip': TOOLTIPS_CONSTANTS.SELECTED_VEHICLE_UI,
                                                   'method': cybersport.CybersportSelectedVehicleToolTipData(contexts.CyberSportUnitContext()).buildToolTip,
                                                   'complex': None},
 TOOLTIPS_CONSTANTS.CYBER_SPORT_SLOT_SELECTED: {'tooltip': TOOLTIPS_CONSTANTS.SELECTED_VEHICLE_UI,
                                                'method': cybersport.CybersportSlotSelectedToolTipData(contexts.CyberSportUnitContext()).buildToolTip,
                                                'complex': None},
 TOOLTIPS_CONSTANTS.CYBER_SPORT_TEAM: {'tooltip': TOOLTIPS_CONSTANTS.UNIT_COMMAND,
                                       'method': cybersport.CybersportUnitToolTipData(contexts.CyberSportUnitContext()).buildToolTip,
                                       'complex': None},
 TOOLTIPS_CONSTANTS.CONTACT: {'tooltip': TOOLTIPS_CONSTANTS.CONTACT_UI,
                              'method': common.ContactTooltipData(contexts.ContactContext()).buildToolTip,
                              'complex': None},
 TOOLTIPS_CONSTANTS.CYBER_SPORT_UNIT_LEVEL: {'tooltip': TOOLTIPS_CONSTANTS.UNIT_LEVEL_UI,
                                             'method': cybersport.CybersportUnitLevelToolTipData(contexts.CyberSportUnitContext()).buildToolTip,
                                             'complex': None},
 TOOLTIPS_CONSTANTS.CYBER_SPORT_VEHICLE_NOT_READY: {'tooltip': TOOLTIPS_CONSTANTS.SELECTED_VEHICLE_UI,
                                                    'method': cybersport.CybersportSlotSelectedToolTipData(contexts.CyberSportUnitContext()).buildToolTip,
                                                    'complex': None},
 TOOLTIPS_CONSTANTS.RSS_NEWS: {'tooltip': TOOLTIPS_CONSTANTS.RSS_NEWS_UI,
                               'method': None,
                               'complex': None},
 TOOLTIPS_CONSTANTS.SORTIE_DIVISION: {'tooltip': TOOLTIPS_CONSTANTS.SORTIE_DIVISION_UI,
                                      'method': common.SortieDivisionTooltipData(contexts.FortificationContext()).buildToolTip,
                                      'complex': None},
 TOOLTIPS_CONSTANTS.FORT_POPOVER_DEFRESPROGRESS: {'tooltip': TOOLTIPS_CONSTANTS.FORT_POPOVER_DEFRESPROGRESS_UI,
                                                  'method': fortifications.FortPopoverDefResTooltipData(contexts.FortPopoverDefResProgressContext()).buildToolTip,
                                                  'complex': None},
 TOOLTIPS_CONSTANTS.FORT_SORTIE_TIME_LIMIT: {'tooltip': TOOLTIPS_CONSTANTS.FORT_SORTIE_TIME_LIMIT_UI,
                                             'method': fortifications.SortiesTimeLimitPacker(contexts.FortSortieLimitContext()).buildToolTip,
                                             'complex': None},
 TOOLTIPS_CONSTANTS.FORT_SORTIE_SERVER_LIMIT: {'tooltip': TOOLTIPS_CONSTANTS.FORT_SORTIE_SERVER_LIMIT_UI,
                                               'method': fortifications.SortiesServerLimitPacker(contexts.FortSortieLimitContext()).buildToolTip,
                                               'complex': None},
 TOOLTIPS_CONSTANTS.CLAN_PROFILE_FORT_BUILDING: {'tooltip': TOOLTIPS_CONSTANTS.FORT_SORTIE_TIME_LIMIT_UI,
                                                 'method': clans.ClanProfileFortBuildingTooltipData(contexts.FortificationContext()).buildToolTip,
                                                 'complex': None},
 TOOLTIPS_CONSTANTS.MAP: {'tooltip': TOOLTIPS_CONSTANTS.MAP_UI,
                          'method': common.MapTooltipData(contexts.HangarContext()).buildToolTip,
                          'complex': None},
 TOOLTIPS_CONSTANTS.HISTORICAL_VEHICLE: {'tooltip': TOOLTIPS_CONSTANTS.VEHICLE_INFO_UI,
                                         'method': vehicle.VehicleInfoTooltipData(contexts.HangarContext()).buildToolTip,
                                         'complex': None},
 TOOLTIPS_CONSTANTS.VEHICLE_PARAMETERS: {'tooltip': TOOLTIPS_CONSTANTS.VEHICLE_PARAMETERS_UI,
                                         'method': vehicle.VehicleParametersTooltipData(contexts.HangarParamContext()).buildToolTip,
                                         'complex': None},
 TOOLTIPS_CONSTANTS.VEHICLE_PREVIEW_PARAMETERS: {'tooltip': TOOLTIPS_CONSTANTS.VEHICLE_PARAMETERS_UI,
                                                 'method': vehicle.VehicleParametersTooltipData(contexts.PreviewParamContext()).buildToolTip,
                                                 'complex': None},
 TOOLTIPS_CONSTANTS.VEHICLE_PREVIEW_CREW_MEMBER: {'tooltip': TOOLTIPS_CONSTANTS.VEHICLE_PREVIEW_CREW_MEMBER_UI,
                                                  'method': vehicle.VehiclePreviewCrewMemberTooltipData(contexts.PreviewContext()).buildToolTip,
                                                  'complex': None},
 TOOLTIPS_CONSTANTS.SETTINGS_CONTROL: {'tooltip': TOOLTIPS_CONSTANTS.COMPLEX_UI,
                                       'method': common.SettingsControlTooltipData(contexts.HangarContext()).buildToolTip,
                                       'complex': lambda data: False},
 TOOLTIPS_CONSTANTS.CLAN_INFO: {'tooltip': TOOLTIPS_CONSTANTS.CLAN_INFO_UI,
                                'method': common.ClanInfoTooltipData(contexts.HangarContext()).buildToolTip,
                                'complex': None},
 TOOLTIPS_CONSTANTS.CLAN_COMMON_INFO: {'tooltip': TOOLTIPS_CONSTANTS.CLAN_COMMON_INFO_UI,
                                       'method': common.ClanCommonInfoTooltipData(contexts.HangarContext()).buildToolTip,
                                       'complex': None},
 TOOLTIPS_CONSTANTS.LADDER_REGULATIONS: {'tooltip': TOOLTIPS_CONSTANTS.LADDER_REGULATIONS_UI,
                                         'method': common.LadderRegulations(contexts.HangarContext()).buildToolTip,
                                         'complex': None},
 TOOLTIPS_CONSTANTS.FORT_BUILDING_INFO: {'tooltip': TOOLTIPS_CONSTANTS.FORT_BUILDING_INFO_UI,
                                         'method': common.ToolTipFortBuildingData(contexts.HangarContext()).buildToolTip,
                                         'complex': None},
 TOOLTIPS_CONSTANTS.REF_SYS_AWARDS: {'tooltip': TOOLTIPS_CONSTANTS.REF_SYS_AWARDS_UI,
                                     'method': common.ToolTipRefSysAwards(contexts.HangarContext()).buildToolTip,
                                     'complex': None},
 TOOLTIPS_CONSTANTS.REF_SYS_DESCRIPTION: {'tooltip': TOOLTIPS_CONSTANTS.REF_SYS_DESCRIPTION_UI,
                                          'method': common.ToolTipRefSysDescription(contexts.HangarContext()).buildToolTip,
                                          'complex': None},
 TOOLTIPS_CONSTANTS.REF_SYS_XP_MULTIPLIER: {'tooltip': TOOLTIPS_CONSTANTS.REF_SYS_XP_MULTIPLIER_UI,
                                            'method': common.ToolTipRefSysXPMultiplier(contexts.HangarContext()).buildToolTip,
                                            'complex': None},
 TOOLTIPS_CONSTANTS.ACTION_PRICE: {'tooltip': TOOLTIPS_CONSTANTS.COMPLEX_UI,
                                   'method': common.ActionTooltipData(contexts.HangarContext()).buildToolTip,
                                   'complex': lambda data: False},
 TOOLTIPS_CONSTANTS.SQUAD_SLOT_VEHICLE_SELECTED: {'tooltip': TOOLTIPS_CONSTANTS.SELECTED_VEHICLE_UI,
                                                  'method': cybersport.SquadSlotSelectedToolTipData(contexts.CyberSportUnitContext()).buildToolTip,
                                                  'complex': None},
 TOOLTIPS_CONSTANTS.SETTINGS_BUTTON: {'tooltip': TOOLTIPS_CONSTANTS.SETTINGS_BUTTON_UI,
                                      'method': common.SettingsButtonTooltipData(contexts.HangarServerStatusContext()).buildToolTip,
                                      'complex': None},
 TOOLTIPS_CONSTANTS.CUSTOMIZATION_ITEM: {'tooltip': TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM_UI,
                                         'method': CustomizationQuestElementTooltip(contexts.TechCustomizationContext()).buildToolTip,
                                         'complex': None},
 TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM: {'tooltip': TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM_UI,
                                              'method': CustomizationElementTooltip(contexts.TechCustomizationContext()).buildToolTip,
                                              'complex': None},
 TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_BONUS: {'tooltip': TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_BONUS_UI,
                                               'method': CustomizationBonusTooltip(contexts.TechCustomizationContext()).buildToolTip,
                                               'complex': None},
 TOOLTIPS_CONSTANTS.FORT_WRONG_TIME: {'tooltip': TOOLTIPS_CONSTANTS.COMPLEX_UI,
                                      'method': common.ToolTipFortWrongTime(contexts.HangarContext()).buildToolTip,
                                      'complex': lambda data: False},
 TOOLTIPS_CONSTANTS.PRIVATE_QUESTS_TILE: {'tooltip': TOOLTIPS_CONSTANTS.PRIVATE_QUESTS_UI,
                                          'method': potapovquests.PrivateQuestsTileTooltipData(contexts.PotapovQuestsTileContext()).buildToolTip,
                                          'complex': None},
 TOOLTIPS_CONSTANTS.PRIVATE_QUESTS_FALLOUT_TILE: {'tooltip': TOOLTIPS_CONSTANTS.PRIVATE_QUESTS_UI,
                                                  'method': potapovquests.PrivateQuestsFalloutTileTooltipData(contexts.PotapovQuestsTileContext()).buildToolTip,
                                                  'complex': None},
 TOOLTIPS_CONSTANTS.PRIVATE_QUESTS_CHAIN: {'tooltip': TOOLTIPS_CONSTANTS.PRIVATE_QUESTS_UI,
                                           'method': potapovquests.PrivateQuestsChainTooltipData(contexts.PotapovQuestsChainContext()).buildToolTip,
                                           'complex': None},
 TOOLTIPS_CONSTANTS.PRIVATE_QUESTS_FEMALE_TANKMAN_AWARD: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                                          'method': potapovquests.FemaleTankmanAwardTooltipData().buildToolTip,
                                                          'complex': None},
 TOOLTIPS_CONSTANTS.PRIVATE_QUESTS_TOKENS_AWARD: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                                  'method': potapovquests.TokensAwardTooltipData().buildToolTip,
                                                  'complex': None},
 TOOLTIPS_CONSTANTS.QUESTS_VEHICLE_BONUSES: {'tooltip': TOOLTIPS_CONSTANTS.COLUMN_FIELDS_UI,
                                             'method': common.QuestVehiclesBonusTooltipData(contexts.QuestContext()).buildToolTip,
                                             'complex': None},
 TOOLTIPS_CONSTANTS.MAP_SMALL: {'tooltip': TOOLTIPS_CONSTANTS.MAP_SMALL_UI,
                                'method': common.MapSmallTooltipData(contexts.FortificationContext()).buildToolTip,
                                'complex': None},
 TOOLTIPS_CONSTANTS.FORT_CONSUMABLE_ORDER: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                            'method': fortifications.FortConsumableOrderTooltipData(contexts.FortOrderContext()).buildToolTip,
                                            'complex': None},
 TOOLTIPS_CONSTANTS.LADDER: {'tooltip': TOOLTIPS_CONSTANTS.LADDER_UI,
                             'method': common.LadderTooltipData(contexts.CyberSportUnitContext()).buildToolTip,
                             'complex': None},
 TOOLTIPS_CONSTANTS.FORT_DIVISION: {'tooltip': TOOLTIPS_CONSTANTS.FORT_DIVISION_UI,
                                    'method': common.FortDivisionTooltipData(contexts.HangarContext()).buildToolTip,
                                    'complex': None},
 TOOLTIPS_CONSTANTS.FORT_SORTIE: {'tooltip': TOOLTIPS_CONSTANTS.FORT_SORTIE_UI,
                                  'method': common.FortSortieTooltipData(contexts.HangarContext()).buildToolTip,
                                  'complex': None},
 TOOLTIPS_CONSTANTS.ENVIRONMENT: {'tooltip': TOOLTIPS_CONSTANTS.ENVIRONMENT_UI,
                                  'method': common.EnvironmentTooltipData(contexts.HangarContext()).buildToolTip,
                                  'complex': None},
 TOOLTIPS_CONSTANTS.SETTINGS_MINIMAP_CIRCLES: {'tooltip': TOOLTIPS_CONSTANTS.SETTINGS_MINIMAP_CIRCLES_UI,
                                               'method': common.SettingsMinimapCircles(contexts.SettingsMinimapContext(None)).buildToolTip,
                                               'complex': None},
 TOOLTIPS_CONSTANTS.SQUAD_RESTRICTIONS_INFO: {'tooltip': TOOLTIPS_CONSTANTS.SQUAD_RESTRICTIONS_INFO_UI,
                                              'method': common.SquadRestrictionsInfo(contexts.SquadRestrictionContext(None)).buildToolTip,
                                              'complex': None},
 TOOLTIPS_CONSTANTS.BOOSTERS_BOOSTER_INFO: {'tooltip': TOOLTIPS_CONSTANTS.BOOSTERS_BOOSTER_INFO_UI,
                                            'method': boosters.BoosterTooltipData(contexts.BoosterContext()).buildToolTip,
                                            'complex': None},
 TOOLTIPS_CONSTANTS.BOOSTERS_SHOP: {'tooltip': TOOLTIPS_CONSTANTS.BOOSTERS_BOOSTER_INFO_UI,
                                    'method': boosters.BoosterTooltipData(contexts.ShopBoosterContext()).buildToolTip,
                                    'complex': None},
 TOOLTIPS_CONSTANTS.BOOSTERS_QUESTS: {'tooltip': TOOLTIPS_CONSTANTS.BOOSTERS_BOOSTER_INFO_UI,
                                      'method': boosters.BoosterTooltipData(contexts.QuestsBoosterContext()).buildToolTip,
                                      'complex': None},
 TOOLTIPS_CONSTANTS.VEHICLE_FILTER: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                     'method': VehicleFilterTooltip(contexts.TechCustomizationContext()).buildToolTip,
                                     'complex': None},
 'default': {'tooltip': TOOLTIPS_CONSTANTS.COMPLEX_UI,
             'method': None,
             'complex': None}}
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\settings\tooltips.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:49:36 St�edn� Evropa (letn� �as)
