# 2016.08.04 20:01:11 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/plat-mac/Carbon/Appearance.py


def FOUR_CHAR_CODE(x):
    return x


kAppearanceEventClass = FOUR_CHAR_CODE('appr')
kAEAppearanceChanged = FOUR_CHAR_CODE('thme')
kAESystemFontChanged = FOUR_CHAR_CODE('sysf')
kAESmallSystemFontChanged = FOUR_CHAR_CODE('ssfn')
kAEViewsFontChanged = FOUR_CHAR_CODE('vfnt')
kThemeDataFileType = FOUR_CHAR_CODE('thme')
kThemePlatinumFileType = FOUR_CHAR_CODE('pltn')
kThemeCustomThemesFileType = FOUR_CHAR_CODE('scen')
kThemeSoundTrackFileType = FOUR_CHAR_CODE('tsnd')
kThemeBrushDialogBackgroundActive = 1
kThemeBrushDialogBackgroundInactive = 2
kThemeBrushAlertBackgroundActive = 3
kThemeBrushAlertBackgroundInactive = 4
kThemeBrushModelessDialogBackgroundActive = 5
kThemeBrushModelessDialogBackgroundInactive = 6
kThemeBrushUtilityWindowBackgroundActive = 7
kThemeBrushUtilityWindowBackgroundInactive = 8
kThemeBrushListViewSortColumnBackground = 9
kThemeBrushListViewBackground = 10
kThemeBrushIconLabelBackground = 11
kThemeBrushListViewSeparator = 12
kThemeBrushChasingArrows = 13
kThemeBrushDragHilite = 14
kThemeBrushDocumentWindowBackground = 15
kThemeBrushFinderWindowBackground = 16
kThemeBrushScrollBarDelimiterActive = 17
kThemeBrushScrollBarDelimiterInactive = 18
kThemeBrushFocusHighlight = 19
kThemeBrushPopupArrowActive = 20
kThemeBrushPopupArrowPressed = 21
kThemeBrushPopupArrowInactive = 22
kThemeBrushAppleGuideCoachmark = 23
kThemeBrushIconLabelBackgroundSelected = 24
kThemeBrushStaticAreaFill = 25
kThemeBrushActiveAreaFill = 26
kThemeBrushButtonFrameActive = 27
kThemeBrushButtonFrameInactive = 28
kThemeBrushButtonFaceActive = 29
kThemeBrushButtonFaceInactive = 30
kThemeBrushButtonFacePressed = 31
kThemeBrushButtonActiveDarkShadow = 32
kThemeBrushButtonActiveDarkHighlight = 33
kThemeBrushButtonActiveLightShadow = 34
kThemeBrushButtonActiveLightHighlight = 35
kThemeBrushButtonInactiveDarkShadow = 36
kThemeBrushButtonInactiveDarkHighlight = 37
kThemeBrushButtonInactiveLightShadow = 38
kThemeBrushButtonInactiveLightHighlight = 39
kThemeBrushButtonPressedDarkShadow = 40
kThemeBrushButtonPressedDarkHighlight = 41
kThemeBrushButtonPressedLightShadow = 42
kThemeBrushButtonPressedLightHighlight = 43
kThemeBrushBevelActiveLight = 44
kThemeBrushBevelActiveDark = 45
kThemeBrushBevelInactiveLight = 46
kThemeBrushBevelInactiveDark = 47
kThemeBrushNotificationWindowBackground = 48
kThemeBrushMovableModalBackground = 49
kThemeBrushSheetBackgroundOpaque = 50
kThemeBrushDrawerBackground = 51
kThemeBrushToolbarBackground = 52
kThemeBrushSheetBackgroundTransparent = 53
kThemeBrushMenuBackground = 54
kThemeBrushMenuBackgroundSelected = 55
kThemeBrushSheetBackground = kThemeBrushSheetBackgroundOpaque
kThemeBrushBlack = -1
kThemeBrushWhite = -2
kThemeBrushPrimaryHighlightColor = -3
kThemeBrushSecondaryHighlightColor = -4
kThemeTextColorDialogActive = 1
kThemeTextColorDialogInactive = 2
kThemeTextColorAlertActive = 3
kThemeTextColorAlertInactive = 4
kThemeTextColorModelessDialogActive = 5
kThemeTextColorModelessDialogInactive = 6
kThemeTextColorWindowHeaderActive = 7
kThemeTextColorWindowHeaderInactive = 8
kThemeTextColorPlacardActive = 9
kThemeTextColorPlacardInactive = 10
kThemeTextColorPlacardPressed = 11
kThemeTextColorPushButtonActive = 12
kThemeTextColorPushButtonInactive = 13
kThemeTextColorPushButtonPressed = 14
kThemeTextColorBevelButtonActive = 15
kThemeTextColorBevelButtonInactive = 16
kThemeTextColorBevelButtonPressed = 17
kThemeTextColorPopupButtonActive = 18
kThemeTextColorPopupButtonInactive = 19
kThemeTextColorPopupButtonPressed = 20
kThemeTextColorIconLabel = 21
kThemeTextColorListView = 22
kThemeTextColorDocumentWindowTitleActive = 23
kThemeTextColorDocumentWindowTitleInactive = 24
kThemeTextColorMovableModalWindowTitleActive = 25
kThemeTextColorMovableModalWindowTitleInactive = 26
kThemeTextColorUtilityWindowTitleActive = 27
kThemeTextColorUtilityWindowTitleInactive = 28
kThemeTextColorPopupWindowTitleActive = 29
kThemeTextColorPopupWindowTitleInactive = 30
kThemeTextColorRootMenuActive = 31
kThemeTextColorRootMenuSelected = 32
kThemeTextColorRootMenuDisabled = 33
kThemeTextColorMenuItemActive = 34
kThemeTextColorMenuItemSelected = 35
kThemeTextColorMenuItemDisabled = 36
kThemeTextColorPopupLabelActive = 37
kThemeTextColorPopupLabelInactive = 38
kThemeTextColorTabFrontActive = 39
kThemeTextColorTabNonFrontActive = 40
kThemeTextColorTabNonFrontPressed = 41
kThemeTextColorTabFrontInactive = 42
kThemeTextColorTabNonFrontInactive = 43
kThemeTextColorIconLabelSelected = 44
kThemeTextColorBevelButtonStickyActive = 45
kThemeTextColorBevelButtonStickyInactive = 46
kThemeTextColorNotification = 47
kThemeTextColorBlack = -1
kThemeTextColorWhite = -2
kThemeStateInactive = 0
kThemeStateActive = 1
kThemeStatePressed = 2
kThemeStateRollover = 6
kThemeStateUnavailable = 7
kThemeStateUnavailableInactive = 8
kThemeStateDisabled = 0
kThemeStatePressedUp = 2
kThemeStatePressedDown = 3
kThemeArrowCursor = 0
kThemeCopyArrowCursor = 1
kThemeAliasArrowCursor = 2
kThemeContextualMenuArrowCursor = 3
kThemeIBeamCursor = 4
kThemeCrossCursor = 5
kThemePlusCursor = 6
kThemeWatchCursor = 7
kThemeClosedHandCursor = 8
kThemeOpenHandCursor = 9
kThemePointingHandCursor = 10
kThemeCountingUpHandCursor = 11
kThemeCountingDownHandCursor = 12
kThemeCountingUpAndDownHandCursor = 13
kThemeSpinningCursor = 14
kThemeResizeLeftCursor = 15
kThemeResizeRightCursor = 16
kThemeResizeLeftRightCursor = 17
kThemeMenuBarNormal = 0
kThemeMenuBarSelected = 1
kThemeMenuSquareMenuBar = 1
kThemeMenuActive = 0
kThemeMenuSelected = 1
kThemeMenuDisabled = 3
kThemeMenuTypePullDown = 0
kThemeMenuTypePopUp = 1
kThemeMenuTypeHierarchical = 2
kThemeMenuTypeInactive = 256
kThemeMenuItemPlain = 0
kThemeMenuItemHierarchical = 1
kThemeMenuItemScrollUpArrow = 2
kThemeMenuItemScrollDownArrow = 3
kThemeMenuItemAtTop = 256
kThemeMenuItemAtBottom = 512
kThemeMenuItemHierBackground = 1024
kThemeMenuItemPopUpBackground = 2048
kThemeMenuItemHasIcon = 32768
kThemeMenuItemNoBackground = 16384
kThemeBackgroundTabPane = 1
kThemeBackgroundPlacard = 2
kThemeBackgroundWindowHeader = 3
kThemeBackgroundListViewWindowHeader = 4
kThemeBackgroundSecondaryGroupBox = 5
kThemeNameTag = FOUR_CHAR_CODE('name')
kThemeVariantNameTag = FOUR_CHAR_CODE('varn')
kThemeVariantBaseTintTag = FOUR_CHAR_CODE('tint')
kThemeHighlightColorTag = FOUR_CHAR_CODE('hcol')
kThemeScrollBarArrowStyleTag = FOUR_CHAR_CODE('sbar')
kThemeScrollBarThumbStyleTag = FOUR_CHAR_CODE('sbth')
kThemeSoundsEnabledTag = FOUR_CHAR_CODE('snds')
kThemeDblClickCollapseTag = FOUR_CHAR_CODE('coll')
kThemeAppearanceFileNameTag = FOUR_CHAR_CODE('thme')
kThemeSystemFontTag = FOUR_CHAR_CODE('lgsf')
kThemeSmallSystemFontTag = FOUR_CHAR_CODE('smsf')
kThemeViewsFontTag = FOUR_CHAR_CODE('vfnt')
kThemeViewsFontSizeTag = FOUR_CHAR_CODE('vfsz')
kThemeDesktopPatternNameTag = FOUR_CHAR_CODE('patn')
kThemeDesktopPatternTag = FOUR_CHAR_CODE('patt')
kThemeDesktopPictureNameTag = FOUR_CHAR_CODE('dpnm')
kThemeDesktopPictureAliasTag = FOUR_CHAR_CODE('dpal')
kThemeDesktopPictureAlignmentTag = FOUR_CHAR_CODE('dpan')
kThemeHighlightColorNameTag = FOUR_CHAR_CODE('hcnm')
kThemeExamplePictureIDTag = FOUR_CHAR_CODE('epic')
kThemeSoundTrackNameTag = FOUR_CHAR_CODE('sndt')
kThemeSoundMaskTag = FOUR_CHAR_CODE('smsk')
kThemeUserDefinedTag = FOUR_CHAR_CODE('user')
kThemeSmoothFontEnabledTag = FOUR_CHAR_CODE('smoo')
kThemeSmoothFontMinSizeTag = FOUR_CHAR_CODE('smos')
kTiledOnScreen = 1
kCenterOnScreen = 2
kFitToScreen = 3
kFillScreen = 4
kUseBestGuess = 5
kThemeCheckBoxClassicX = 0
kThemeCheckBoxCheckMark = 1
kThemeScrollBarArrowsSingle = 0
kThemeScrollBarArrowsLowerRight = 1
kThemeScrollBarThumbNormal = 0
kThemeScrollBarThumbProportional = 1
kThemeSystemFont = 0
kThemeSmallSystemFont = 1
kThemeSmallEmphasizedSystemFont = 2
kThemeViewsFont = 3
kThemeEmphasizedSystemFont = 4
kThemeApplicationFont = 5
kThemeLabelFont = 6
kThemeMenuTitleFont = 100
kThemeMenuItemFont = 101
kThemeMenuItemMarkFont = 102
kThemeMenuItemCmdKeyFont = 103
kThemeWindowTitleFont = 104
kThemePushButtonFont = 105
kThemeUtilityWindowTitleFont = 106
kThemeAlertHeaderFont = 107
kThemeCurrentPortFont = 200
kThemeTabNonFront = 0
kThemeTabNonFrontPressed = 1
kThemeTabNonFrontInactive = 2
kThemeTabFront = 3
kThemeTabFrontInactive = 4
kThemeTabNonFrontUnavailable = 5
kThemeTabFrontUnavailable = 6
kThemeTabNorth = 0
kThemeTabSouth = 1
kThemeTabEast = 2
kThemeTabWest = 3
kThemeSmallTabHeight = 16
kThemeLargeTabHeight = 21
kThemeTabPaneOverlap = 3
kThemeSmallTabHeightMax = 19
kThemeLargeTabHeightMax = 24
kThemeMediumScrollBar = 0
kThemeSmallScrollBar = 1
kThemeMediumSlider = 2
kThemeMediumProgressBar = 3
kThemeMediumIndeterminateBar = 4
kThemeRelevanceBar = 5
kThemeSmallSlider = 6
kThemeLargeProgressBar = 7
kThemeLargeIndeterminateBar = 8
kThemeTrackActive = 0
kThemeTrackDisabled = 1
kThemeTrackNothingToScroll = 2
kThemeTrackInactive = 3
kThemeLeftOutsideArrowPressed = 1
kThemeLeftInsideArrowPressed = 2
kThemeLeftTrackPressed = 4
kThemeThumbPressed = 8
kThemeRightTrackPressed = 16
kThemeRightInsideArrowPressed = 32
kThemeRightOutsideArrowPressed = 64
kThemeTopOutsideArrowPressed = kThemeLeftOutsideArrowPressed
kThemeTopInsideArrowPressed = kThemeLeftInsideArrowPressed
kThemeTopTrackPressed = kThemeLeftTrackPressed
kThemeBottomTrackPressed = kThemeRightTrackPressed
kThemeBottomInsideArrowPressed = kThemeRightInsideArrowPressed
kThemeBottomOutsideArrowPressed = kThemeRightOutsideArrowPressed
kThemeThumbPlain = 0
kThemeThumbUpward = 1
kThemeThumbDownward = 2
kThemeTrackHorizontal = 1
kThemeTrackRightToLeft = 2
kThemeTrackShowThumb = 4
kThemeTrackThumbRgnIsNotGhost = 8
kThemeTrackNoScrollBarArrows = 16
kThemeWindowHasGrow = 1
kThemeWindowHasHorizontalZoom = 8
kThemeWindowHasVerticalZoom = 16
kThemeWindowHasFullZoom = kThemeWindowHasHorizontalZoom + kThemeWindowHasVerticalZoom
kThemeWindowHasCloseBox = 32
kThemeWindowHasCollapseBox = 64
kThemeWindowHasTitleText = 128
kThemeWindowIsCollapsed = 256
kThemeWindowHasDirty = 512
kThemeDocumentWindow = 0
kThemeDialogWindow = 1
kThemeMovableDialogWindow = 2
kThemeAlertWindow = 3
kThemeMovableAlertWindow = 4
kThemePlainDialogWindow = 5
kThemeShadowDialogWindow = 6
kThemePopupWindow = 7
kThemeUtilityWindow = 8
kThemeUtilitySideWindow = 9
kThemeSheetWindow = 10
kThemeDrawerWindow = 11
kThemeWidgetCloseBox = 0
kThemeWidgetZoomBox = 1
kThemeWidgetCollapseBox = 2
kThemeWidgetDirtyCloseBox = 6
kThemeArrowLeft = 0
kThemeArrowDown = 1
kThemeArrowRight = 2
kThemeArrowUp = 3
kThemeArrow3pt = 0
kThemeArrow5pt = 1
kThemeArrow7pt = 2
kThemeArrow9pt = 3
kThemeGrowLeft = 1
kThemeGrowRight = 2
kThemeGrowUp = 4
kThemeGrowDown = 8
kThemePushButton = 0
kThemeCheckBox = 1
kThemeRadioButton = 2
kThemeBevelButton = 3
kThemeArrowButton = 4
kThemePopupButton = 5
kThemeDisclosureButton = 6
kThemeIncDecButton = 7
kThemeSmallBevelButton = 8
kThemeMediumBevelButton = 3
kThemeLargeBevelButton = 9
kThemeListHeaderButton = 10
kThemeRoundButton = 11
kThemeLargeRoundButton = 12
kThemeSmallCheckBox = 13
kThemeSmallRadioButton = 14
kThemeRoundedBevelButton = 15
kThemeNormalCheckBox = kThemeCheckBox
kThemeNormalRadioButton = kThemeRadioButton
kThemeButtonOff = 0
kThemeButtonOn = 1
kThemeButtonMixed = 2
kThemeDisclosureRight = 0
kThemeDisclosureDown = 1
kThemeDisclosureLeft = 2
kThemeAdornmentNone = 0
kThemeAdornmentDefault = 1
kThemeAdornmentFocus = 4
kThemeAdornmentRightToLeft = 16
kThemeAdornmentDrawIndicatorOnly = 32
kThemeAdornmentHeaderButtonLeftNeighborSelected = 64
kThemeAdornmentHeaderButtonRightNeighborSelected = 128
kThemeAdornmentHeaderButtonSortUp = 256
kThemeAdornmentHeaderMenuButton = 512
kThemeAdornmentHeaderButtonNoShadow = 1024
kThemeAdornmentHeaderButtonShadowOnly = 2048
kThemeAdornmentNoShadow = kThemeAdornmentHeaderButtonNoShadow
kThemeAdornmentShadowOnly = kThemeAdornmentHeaderButtonShadowOnly
kThemeAdornmentArrowLeftArrow = 64
kThemeAdornmentArrowDownArrow = 128
kThemeAdornmentArrowDoubleArrow = 256
kThemeAdornmentArrowUpArrow = 512
kThemeNoSounds = 0
kThemeWindowSoundsMask = 1
kThemeMenuSoundsMask = 2
kThemeControlSoundsMask = 4
kThemeFinderSoundsMask = 8
kThemeDragSoundNone = 0
kThemeDragSoundMoveWindow = FOUR_CHAR_CODE('wmov')
kThemeDragSoundGrowWindow = FOUR_CHAR_CODE('wgro')
kThemeDragSoundMoveUtilWindow = FOUR_CHAR_CODE('umov')
kThemeDragSoundGrowUtilWindow = FOUR_CHAR_CODE('ugro')
kThemeDragSoundMoveDialog = FOUR_CHAR_CODE('dmov')
kThemeDragSoundMoveAlert = FOUR_CHAR_CODE('amov')
kThemeDragSoundMoveIcon = FOUR_CHAR_CODE('imov')
kThemeDragSoundSliderThumb = FOUR_CHAR_CODE('slth')
kThemeDragSoundSliderGhost = FOUR_CHAR_CODE('slgh')
kThemeDragSoundScrollBarThumb = FOUR_CHAR_CODE('sbth')
kThemeDragSoundScrollBarGhost = FOUR_CHAR_CODE('sbgh')
kThemeDragSoundScrollBarArrowDecreasing = FOUR_CHAR_CODE('sbad')
kThemeDragSoundScrollBarArrowIncreasing = FOUR_CHAR_CODE('sbai')
kThemeDragSoundDragging = FOUR_CHAR_CODE('drag')
kThemeSoundNone = 0
kThemeSoundMenuOpen = FOUR_CHAR_CODE('mnuo')
kThemeSoundMenuClose = FOUR_CHAR_CODE('mnuc')
kThemeSoundMenuItemHilite = FOUR_CHAR_CODE('mnui')
kThemeSoundMenuItemRelease = FOUR_CHAR_CODE('mnus')
kThemeSoundWindowClosePress = FOUR_CHAR_CODE('wclp')
kThemeSoundWindowCloseEnter = FOUR_CHAR_CODE('wcle')
kThemeSoundWindowCloseExit = FOUR_CHAR_CODE('wclx')
kThemeSoundWindowCloseRelease = FOUR_CHAR_CODE('wclr')
kThemeSoundWindowZoomPress = FOUR_CHAR_CODE('wzmp')
kThemeSoundWindowZoomEnter = FOUR_CHAR_CODE('wzme')
kThemeSoundWindowZoomExit = FOUR_CHAR_CODE('wzmx')
kThemeSoundWindowZoomRelease = FOUR_CHAR_CODE('wzmr')
kThemeSoundWindowCollapsePress = FOUR_CHAR_CODE('wcop')
kThemeSoundWindowCollapseEnter = FOUR_CHAR_CODE('wcoe')
kThemeSoundWindowCollapseExit = FOUR_CHAR_CODE('wcox')
kThemeSoundWindowCollapseRelease = FOUR_CHAR_CODE('wcor')
kThemeSoundWindowDragBoundary = FOUR_CHAR_CODE('wdbd')
kThemeSoundUtilWinClosePress = FOUR_CHAR_CODE('uclp')
kThemeSoundUtilWinCloseEnter = FOUR_CHAR_CODE('ucle')
kThemeSoundUtilWinCloseExit = FOUR_CHAR_CODE('uclx')
kThemeSoundUtilWinCloseRelease = FOUR_CHAR_CODE('uclr')
kThemeSoundUtilWinZoomPress = FOUR_CHAR_CODE('uzmp')
kThemeSoundUtilWinZoomEnter = FOUR_CHAR_CODE('uzme')
kThemeSoundUtilWinZoomExit = FOUR_CHAR_CODE('uzmx')
kThemeSoundUtilWinZoomRelease = FOUR_CHAR_CODE('uzmr')
kThemeSoundUtilWinCollapsePress = FOUR_CHAR_CODE('ucop')
kThemeSoundUtilWinCollapseEnter = FOUR_CHAR_CODE('ucoe')
kThemeSoundUtilWinCollapseExit = FOUR_CHAR_CODE('ucox')
kThemeSoundUtilWinCollapseRelease = FOUR_CHAR_CODE('ucor')
kThemeSoundUtilWinDragBoundary = FOUR_CHAR_CODE('udbd')
kThemeSoundWindowOpen = FOUR_CHAR_CODE('wopn')
kThemeSoundWindowClose = FOUR_CHAR_CODE('wcls')
kThemeSoundWindowZoomIn = FOUR_CHAR_CODE('wzmi')
kThemeSoundWindowZoomOut = FOUR_CHAR_CODE('wzmo')
kThemeSoundWindowCollapseUp = FOUR_CHAR_CODE('wcol')
kThemeSoundWindowCollapseDown = FOUR_CHAR_CODE('wexp')
kThemeSoundWindowActivate = FOUR_CHAR_CODE('wact')
kThemeSoundUtilWindowOpen = FOUR_CHAR_CODE('uopn')
kThemeSoundUtilWindowClose = FOUR_CHAR_CODE('ucls')
kThemeSoundUtilWindowZoomIn = FOUR_CHAR_CODE('uzmi')
kThemeSoundUtilWindowZoomOut = FOUR_CHAR_CODE('uzmo')
kThemeSoundUtilWindowCollapseUp = FOUR_CHAR_CODE('ucol')
kThemeSoundUtilWindowCollapseDown = FOUR_CHAR_CODE('uexp')
kThemeSoundUtilWindowActivate = FOUR_CHAR_CODE('uact')
kThemeSoundDialogOpen = FOUR_CHAR_CODE('dopn')
kThemeSoundDialogClose = FOUR_CHAR_CODE('dlgc')
kThemeSoundAlertOpen = FOUR_CHAR_CODE('aopn')
kThemeSoundAlertClose = FOUR_CHAR_CODE('altc')
kThemeSoundPopupWindowOpen = FOUR_CHAR_CODE('pwop')
kThemeSoundPopupWindowClose = FOUR_CHAR_CODE('pwcl')
kThemeSoundButtonPress = FOUR_CHAR_CODE('btnp')
kThemeSoundButtonEnter = FOUR_CHAR_CODE('btne')
kThemeSoundButtonExit = FOUR_CHAR_CODE('btnx')
kThemeSoundButtonRelease = FOUR_CHAR_CODE('btnr')
kThemeSoundDefaultButtonPress = FOUR_CHAR_CODE('dbtp')
kThemeSoundDefaultButtonEnter = FOUR_CHAR_CODE('dbte')
kThemeSoundDefaultButtonExit = FOUR_CHAR_CODE('dbtx')
kThemeSoundDefaultButtonRelease = FOUR_CHAR_CODE('dbtr')
kThemeSoundCancelButtonPress = FOUR_CHAR_CODE('cbtp')
kThemeSoundCancelButtonEnter = FOUR_CHAR_CODE('cbte')
kThemeSoundCancelButtonExit = FOUR_CHAR_CODE('cbtx')
kThemeSoundCancelButtonRelease = FOUR_CHAR_CODE('cbtr')
kThemeSoundCheckboxPress = FOUR_CHAR_CODE('chkp')
kThemeSoundCheckboxEnter = FOUR_CHAR_CODE('chke')
kThemeSoundCheckboxExit = FOUR_CHAR_CODE('chkx')
kThemeSoundCheckboxRelease = FOUR_CHAR_CODE('chkr')
kThemeSoundRadioPress = FOUR_CHAR_CODE('radp')
kThemeSoundRadioEnter = FOUR_CHAR_CODE('rade')
kThemeSoundRadioExit = FOUR_CHAR_CODE('radx')
kThemeSoundRadioRelease = FOUR_CHAR_CODE('radr')
kThemeSoundScrollArrowPress = FOUR_CHAR_CODE('sbap')
kThemeSoundScrollArrowEnter = FOUR_CHAR_CODE('sbae')
kThemeSoundScrollArrowExit = FOUR_CHAR_CODE('sbax')
kThemeSoundScrollArrowRelease = FOUR_CHAR_CODE('sbar')
kThemeSoundScrollEndOfTrack = FOUR_CHAR_CODE('sbte')
kThemeSoundScrollTrackPress = FOUR_CHAR_CODE('sbtp')
kThemeSoundSliderEndOfTrack = FOUR_CHAR_CODE('slte')
kThemeSoundSliderTrackPress = FOUR_CHAR_CODE('sltp')
kThemeSoundBalloonOpen = FOUR_CHAR_CODE('blno')
kThemeSoundBalloonClose = FOUR_CHAR_CODE('blnc')
kThemeSoundBevelPress = FOUR_CHAR_CODE('bevp')
kThemeSoundBevelEnter = FOUR_CHAR_CODE('beve')
kThemeSoundBevelExit = FOUR_CHAR_CODE('bevx')
kThemeSoundBevelRelease = FOUR_CHAR_CODE('bevr')
kThemeSoundLittleArrowUpPress = FOUR_CHAR_CODE('laup')
kThemeSoundLittleArrowDnPress = FOUR_CHAR_CODE('ladp')
kThemeSoundLittleArrowEnter = FOUR_CHAR_CODE('lare')
kThemeSoundLittleArrowExit = FOUR_CHAR_CODE('larx')
kThemeSoundLittleArrowUpRelease = FOUR_CHAR_CODE('laur')
kThemeSoundLittleArrowDnRelease = FOUR_CHAR_CODE('ladr')
kThemeSoundPopupPress = FOUR_CHAR_CODE('popp')
kThemeSoundPopupEnter = FOUR_CHAR_CODE('pope')
kThemeSoundPopupExit = FOUR_CHAR_CODE('popx')
kThemeSoundPopupRelease = FOUR_CHAR_CODE('popr')
kThemeSoundDisclosurePress = FOUR_CHAR_CODE('dscp')
kThemeSoundDisclosureEnter = FOUR_CHAR_CODE('dsce')
kThemeSoundDisclosureExit = FOUR_CHAR_CODE('dscx')
kThemeSoundDisclosureRelease = FOUR_CHAR_CODE('dscr')
kThemeSoundTabPressed = FOUR_CHAR_CODE('tabp')
kThemeSoundTabEnter = FOUR_CHAR_CODE('tabe')
kThemeSoundTabExit = FOUR_CHAR_CODE('tabx')
kThemeSoundTabRelease = FOUR_CHAR_CODE('tabr')
kThemeSoundDragTargetHilite = FOUR_CHAR_CODE('dthi')
kThemeSoundDragTargetUnhilite = FOUR_CHAR_CODE('dtuh')
kThemeSoundDragTargetDrop = FOUR_CHAR_CODE('dtdr')
kThemeSoundEmptyTrash = FOUR_CHAR_CODE('ftrs')
kThemeSoundSelectItem = FOUR_CHAR_CODE('fsel')
kThemeSoundNewItem = FOUR_CHAR_CODE('fnew')
kThemeSoundReceiveDrop = FOUR_CHAR_CODE('fdrp')
kThemeSoundCopyDone = FOUR_CHAR_CODE('fcpd')
kThemeSoundResolveAlias = FOUR_CHAR_CODE('fral')
kThemeSoundLaunchApp = FOUR_CHAR_CODE('flap')
kThemeSoundDiskInsert = FOUR_CHAR_CODE('dski')
kThemeSoundDiskEject = FOUR_CHAR_CODE('dske')
kThemeSoundFinderDragOnIcon = FOUR_CHAR_CODE('fdon')
kThemeSoundFinderDragOffIcon = FOUR_CHAR_CODE('fdof')
kThemePopupTabNormalPosition = 0
kThemePopupTabCenterOnWindow = 1
kThemePopupTabCenterOnOffset = 2
kThemeMetricScrollBarWidth = 0
kThemeMetricSmallScrollBarWidth = 1
kThemeMetricCheckBoxHeight = 2
kThemeMetricRadioButtonHeight = 3
kThemeMetricEditTextWhitespace = 4
kThemeMetricEditTextFrameOutset = 5
kThemeMetricListBoxFrameOutset = 6
kThemeMetricFocusRectOutset = 7
kThemeMetricImageWellThickness = 8
kThemeMetricScrollBarOverlap = 9
kThemeMetricLargeTabHeight = 10
kThemeMetricLargeTabCapsWidth = 11
kThemeMetricTabFrameOverlap = 12
kThemeMetricTabIndentOrStyle = 13
kThemeMetricTabOverlap = 14
kThemeMetricSmallTabHeight = 15
kThemeMetricSmallTabCapsWidth = 16
kThemeMetricDisclosureButtonHeight = 17
kThemeMetricRoundButtonSize = 18
kThemeMetricPushButtonHeight = 19
kThemeMetricListHeaderHeight = 20
kThemeMetricSmallCheckBoxHeight = 21
kThemeMetricDisclosureButtonWidth = 22
kThemeMetricSmallDisclosureButtonHeight = 23
kThemeMetricSmallDisclosureButtonWidth = 24
kThemeMetricDisclosureTriangleHeight = 25
kThemeMetricDisclosureTriangleWidth = 26
kThemeMetricLittleArrowsHeight = 27
kThemeMetricLittleArrowsWidth = 28
kThemeMetricPaneSplitterHeight = 29
kThemeMetricPopupButtonHeight = 30
kThemeMetricSmallPopupButtonHeight = 31
kThemeMetricLargeProgressBarThickness = 32
kThemeMetricPullDownHeight = 33
kThemeMetricSmallPullDownHeight = 34
kThemeMetricSmallPushButtonHeight = 35
kThemeMetricSmallRadioButtonHeight = 36
kThemeMetricRelevanceIndicatorHeight = 37
kThemeMetricResizeControlHeight = 38
kThemeMetricSmallResizeControlHeight = 39
kThemeMetricLargeRoundButtonSize = 40
kThemeMetricHSliderHeight = 41
kThemeMetricHSliderTickHeight = 42
kThemeMetricSmallHSliderHeight = 43
kThemeMetricSmallHSliderTickHeight = 44
kThemeMetricVSliderWidth = 45
kThemeMetricVSliderTickWidth = 46
kThemeMetricSmallVSliderWidth = 47
kThemeMetricSmallVSliderTickWidth = 48
kThemeMetricTitleBarControlsHeight = 49
kThemeMetricCheckBoxWidth = 50
kThemeMetricSmallCheckBoxWidth = 51
kThemeMetricRadioButtonWidth = 52
kThemeMetricSmallRadioButtonWidth = 53
kThemeMetricSmallHSliderMinThumbWidth = 54
kThemeMetricSmallVSliderMinThumbHeight = 55
kThemeMetricSmallHSliderTickOffset = 56
kThemeMetricSmallVSliderTickOffset = 57
kThemeMetricNormalProgressBarThickness = 58
kThemeMetricProgressBarShadowOutset = 59
kThemeMetricSmallProgressBarShadowOutset = 60
kThemeMetricPrimaryGroupBoxContentInset = 61
kThemeMetricSecondaryGroupBoxContentInset = 62
kThemeMetricMenuMarkColumnWidth = 63
kThemeMetricMenuExcludedMarkColumnWidth = 64
kThemeMetricMenuMarkIndent = 65
kThemeMetricMenuTextLeadingEdgeMargin = 66
kThemeMetricMenuTextTrailingEdgeMargin = 67
kThemeMetricMenuIndentWidth = 68
kThemeMetricMenuIconTrailingEdgeMargin = 69
kThemeActiveDialogBackgroundBrush = kThemeBrushDialogBackgroundActive
kThemeInactiveDialogBackgroundBrush = kThemeBrushDialogBackgroundInactive
kThemeActiveAlertBackgroundBrush = kThemeBrushAlertBackgroundActive
kThemeInactiveAlertBackgroundBrush = kThemeBrushAlertBackgroundInactive
kThemeActiveModelessDialogBackgroundBrush = kThemeBrushModelessDialogBackgroundActive
kThemeInactiveModelessDialogBackgroundBrush = kThemeBrushModelessDialogBackgroundInactive
kThemeActiveUtilityWindowBackgroundBrush = kThemeBrushUtilityWindowBackgroundActive
kThemeInactiveUtilityWindowBackgroundBrush = kThemeBrushUtilityWindowBackgroundInactive
kThemeListViewSortColumnBackgroundBrush = kThemeBrushListViewSortColumnBackground
kThemeListViewBackgroundBrush = kThemeBrushListViewBackground
kThemeIconLabelBackgroundBrush = kThemeBrushIconLabelBackground
kThemeListViewSeparatorBrush = kThemeBrushListViewSeparator
kThemeChasingArrowsBrush = kThemeBrushChasingArrows
kThemeDragHiliteBrush = kThemeBrushDragHilite
kThemeDocumentWindowBackgroundBrush = kThemeBrushDocumentWindowBackground
kThemeFinderWindowBackgroundBrush = kThemeBrushFinderWindowBackground
kThemeActiveScrollBarDelimiterBrush = kThemeBrushScrollBarDelimiterActive
kThemeInactiveScrollBarDelimiterBrush = kThemeBrushScrollBarDelimiterInactive
kThemeFocusHighlightBrush = kThemeBrushFocusHighlight
kThemeActivePopupArrowBrush = kThemeBrushPopupArrowActive
kThemePressedPopupArrowBrush = kThemeBrushPopupArrowPressed
kThemeInactivePopupArrowBrush = kThemeBrushPopupArrowInactive
kThemeAppleGuideCoachmarkBrush = kThemeBrushAppleGuideCoachmark
kThemeActiveDialogTextColor = kThemeTextColorDialogActive
kThemeInactiveDialogTextColor = kThemeTextColorDialogInactive
kThemeActiveAlertTextColor = kThemeTextColorAlertActive
kThemeInactiveAlertTextColor = kThemeTextColorAlertInactive
kThemeActiveModelessDialogTextColor = kThemeTextColorModelessDialogActive
kThemeInactiveModelessDialogTextColor = kThemeTextColorModelessDialogInactive
kThemeActiveWindowHeaderTextColor = kThemeTextColorWindowHeaderActive
kThemeInactiveWindowHeaderTextColor = kThemeTextColorWindowHeaderInactive
kThemeActivePlacardTextColor = kThemeTextColorPlacardActive
kThemeInactivePlacardTextColor = kThemeTextColorPlacardInactive
kThemePressedPlacardTextColor = kThemeTextColorPlacardPressed
kThemeActivePushButtonTextColor = kThemeTextColorPushButtonActive
kThemeInactivePushButtonTextColor = kThemeTextColorPushButtonInactive
kThemePressedPushButtonTextColor = kThemeTextColorPushButtonPressed
kThemeActiveBevelButtonTextColor = kThemeTextColorBevelButtonActive
kThemeInactiveBevelButtonTextColor = kThemeTextColorBevelButtonInactive
kThemePressedBevelButtonTextColor = kThemeTextColorBevelButtonPressed
kThemeActivePopupButtonTextColor = kThemeTextColorPopupButtonActive
kThemeInactivePopupButtonTextColor = kThemeTextColorPopupButtonInactive
kThemePressedPopupButtonTextColor = kThemeTextColorPopupButtonPressed
kThemeIconLabelTextColor = kThemeTextColorIconLabel
kThemeListViewTextColor = kThemeTextColorListView
kThemeActiveDocumentWindowTitleTextColor = kThemeTextColorDocumentWindowTitleActive
kThemeInactiveDocumentWindowTitleTextColor = kThemeTextColorDocumentWindowTitleInactive
kThemeActiveMovableModalWindowTitleTextColor = kThemeTextColorMovableModalWindowTitleActive
kThemeInactiveMovableModalWindowTitleTextColor = kThemeTextColorMovableModalWindowTitleInactive
kThemeActiveUtilityWindowTitleTextColor = kThemeTextColorUtilityWindowTitleActive
kThemeInactiveUtilityWindowTitleTextColor = kThemeTextColorUtilityWindowTitleInactive
kThemeActivePopupWindowTitleColor = kThemeTextColorPopupWindowTitleActive
kThemeInactivePopupWindowTitleColor = kThemeTextColorPopupWindowTitleInactive
kThemeActiveRootMenuTextColor = kThemeTextColorRootMenuActive
kThemeSelectedRootMenuTextColor = kThemeTextColorRootMenuSelected
kThemeDisabledRootMenuTextColor = kThemeTextColorRootMenuDisabled
kThemeActiveMenuItemTextColor = kThemeTextColorMenuItemActive
kThemeSelectedMenuItemTextColor = kThemeTextColorMenuItemSelected
kThemeDisabledMenuItemTextColor = kThemeTextColorMenuItemDisabled
kThemeActivePopupLabelTextColor = kThemeTextColorPopupLabelActive
kThemeInactivePopupLabelTextColor = kThemeTextColorPopupLabelInactive
kAEThemeSwitch = kAEAppearanceChanged
kThemeNoAdornment = kThemeAdornmentNone
kThemeDefaultAdornment = kThemeAdornmentDefault
kThemeFocusAdornment = kThemeAdornmentFocus
kThemeRightToLeftAdornment = kThemeAdornmentRightToLeft
kThemeDrawIndicatorOnly = kThemeAdornmentDrawIndicatorOnly
kThemeBrushPassiveAreaFill = kThemeBrushStaticAreaFill
kThemeMetricCheckBoxGlyphHeight = kThemeMetricCheckBoxHeight
kThemeMetricRadioButtonGlyphHeight = kThemeMetricRadioButtonHeight
kThemeMetricDisclosureButtonSize = kThemeMetricDisclosureButtonHeight
kThemeMetricBestListHeaderHeight = kThemeMetricListHeaderHeight
kThemeMetricSmallProgressBarThickness = kThemeMetricNormalProgressBarThickness
kThemeMetricProgressBarThickness = kThemeMetricLargeProgressBarThickness
kThemeScrollBar = kThemeMediumScrollBar
kThemeSlider = kThemeMediumSlider
kThemeProgressBar = kThemeMediumProgressBar
kThemeIndeterminateBar = kThemeMediumIndeterminateBar
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\plat-mac\carbon\appearance.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 20:01:11 St�edn� Evropa (letn� �as)
