# 2016.08.04 19:47:46 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/Settings.py
import BigWorld
g_instance = None
KEY_UPDATE_URL = 'updateUrl'
KEY_CONTROL_MODE = 'controlMode'
KEY_LOGIN_INFO = 'loginInfo'
KEY_SCREEN_SIZE = 'screenSize'
KEY_VIDEO_MODE = 'videoMode'
KEY_LOBBY_TOOLTIP_DELAY = 'lobbyTooltipDelay'
KEY_SOUND_PREFERENCES = 'soundPrefs'
KEY_REPLAY_PREFERENCES = 'replayPrefs'
APPLICATION_CLOSE_DELAY = 'closeApplicationDelay'
KEY_MESSENGER_PREFERENCES = 'messengerPrefs'
KEY_LOGINPAGE_PREFERENCES = 'loginPage'
KEY_ACCOUNT_SETTINGS = 'accounts'
KEY_COMMAND_MAPPING = 'commandMapping'
KEY_SHOW_STARTUP_MOVIE = 'showStartupMovie'
KEY_VOIP_DEVICE = 'captureDevice'
KEY_VIBRATION = 'vibration'
KEY_ENABLE_EDGE_DETECT_AA = 'enableEdgeDetectAA'
KEY_ENABLE_MORTEM_POST_EFFECT_OLD = 'enableMortemPostEffect'
KEY_ENABLE_MORTEM_POST_EFFECT = 'enablePostMortemEffect'
KEY_WINDOWS_STORED_DATA = 'windowsStoredData'
KEY_FOV = 'fov'
KEY_GUI_NOTIFY_INFO = 'guiNotifyInfo'
KEY_DYNAMIC_FOV = 'dynamicFov'
KEY_DYNAMIC_FOV_ENABLED = 'dynamicFovEnabled'
INTRO_VIDEO_VERSION = 'introVideoVersion'

class Settings(object):

    def __init__(self, scriptConfig, engineConfig, userPrefs):
        self.scriptConfig = scriptConfig
        self.engineConfig = engineConfig
        self.userPrefs = userPrefs

    def save(self):
        BigWorld.savePreferences()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\settings.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:47:46 St�edn� Evropa (letn� �as)
