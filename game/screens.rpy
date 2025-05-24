################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    unscrollable "hide"

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    unscrollable "hide"

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"

style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
  zorder 4
  style_prefix "input"

  frame:
    ypadding 20
    xpadding 20
    xanchor 1.0
    yanchor 0.0
    xpos 1916
    ypos 360

    vbox:
      xsize 372
      yfill False
      ymaximum 675
      text prompt style "input_prompt"
      null height 20
      input id "input" text_align 0.5

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## http://www.renpy.org/doc/html/screen_special.html#choice



## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = False

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            #textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save") text_selected_color "#912623"

        textbutton _("Load") action ShowMenu("load") text_selected_color "#32495C"

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("Content Advisory") action ShowMenu('content_advisory')

        textbutton _("Discord") action OpenURL("https://discord.gg/PcJPK7G")

        if not main_menu:

            textbutton _("Model Credits") action ShowMenu('model_credits')

        textbutton _("Credits") action ShowMenu("about")

        if renpy.variant("pc"):

            ## Help isn't necessary or relevant to mobile devices.
            #textbutton _("Help") action ShowMenu("help")

            ## The quit button is banned on iOS and unnecessary on Android.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 1920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Credits")):

        style_prefix "about"

        vbox:
            xpos 150
            xsize 1350

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]\n\n")

            label "Team\n"

            #grid 2 16:
            grid 2 16:
                xspacing 60
                text _("Project Lead")
                text _("Wife Trainer")
                text _("Lead Programmer")
                text _("Digital Bonsai")
                text _("Community Manager")
                text _("Semeicardia")
                text _("Lead Content Importer")
                text _("A4hryou")
                text _("Initial Development Contributor")
                text _("DJ")
                text _("Content Importer")
                text _("Blank Subroutine")
                text _("Content Importer")
                text _("Blubblegum")
                text _("Content Importer")
                text _("HeavyEavy")
                text _("Content Importer")
                text _("John of Liedenfrost")
                text _("Content Importer")
                text _("The Fiduciary")
                text _("Content Importer")
                text _("SelectivePaperClip")
                text _("Content Importer")
                text _("Subli")
                text _("Content Importer & Playtester")
                text _("Apropos de Nada")
                text _("Playtester")
                text _("VikingCrawler")
                text _("Playtester")
                text _("Tristimdorion")
                text _("Graphical Assets")
                text _("Paul")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text:
    size 30


style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                xspacing gui.slot_spacing_x
                yspacing gui.slot_spacing_y

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        background ("#91262355" if title == 'Save' else "#32495C55")
                        action If(title=='Save', (SetVariable('save_name', ''), ShowTransient('ask_save_name', slot=slot)), FileAction(slot))

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        null height 8

                        # text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                        text FileTime(slot, format=_("{#file_time}%b %d, %Y %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"
                            hover_color "#FFF"

                        text FileSaveName(slot):
                            style "slot_name_text"
                            hover_color "#FFF"

                        key "save_delete" action FileDelete(slot)

                        if FileLoadable(slot):
                            imagebutton:
                                idle "gui/delete_save_idle.png"
                                hover "gui/delete_save_hover.png"
                                action FileDelete(slot)
                                xpos 360
                                ypos -250
                                xanchor 0.5
                                yanchor 0.5

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()

screen ask_save_name(slot):
    style_prefix "confirm"
    zorder 1000
    modal True

    key 'K_RETURN' action (Hide('ask_save_name'), FileSave(slot))
    key 'K_KP_ENTER' action (Hide('ask_save_name'), FileSave(slot))

    frame:
        padding(50, 50, 20, 50)
        align (0.5, 0.5)
        has vbox

        label "Please give a name to the saved game" style "confirm_prompt"
        text "(Maximum length 25 characters)" xalign 0.5 size 16
        null height 20
        input value VariableInputValue('save_name') length 25 xalign 0.5
        null height 20
        hbox:
            xalign 0.5
            spacing 50
            textbutton 'Accept(Enter)' action (Hide('ask_save_name'), FileSave(slot)) text_color "#DDD" text_hover_color "#CC6600"
            textbutton 'Cancel' action Hide('ask_save_name') text_color "#DDD" text_hover_color "#CC6600"


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:
            xpos 150
            ypos 80

            hbox:
                box_wrap True
                box_wrap_spacing 10

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                # vbox:
                #     style_prefix "radio"
                #     label _("Rollback Side")
                #     textbutton _("Disable") action Preference("rollback side", "disable")
                #     textbutton _("Left") action Preference("rollback side", "left")
                #     textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle") ymaximum 100
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.
                vbox:
                    style_prefix "check"
                    label _("Notify")
                    text _("Notify Time ([persistent.notify_on_screen_time:.2])")
                    bar value FieldValue(persistent, 'notify_on_screen_time', 9.8, offset = 0.1, step = 0.1) xmaximum 300
                    null height 10
                    textbutton _("Notify on Popup") action ToggleField(persistent, "notify_to_popup")
                    textbutton _("Notify on History") action ToggleField(persistent, "notify_to_history_box")

                vbox:
                    style_prefix "check"
                    label _("Images")
                    textbutton _("Resize Images") action ToggleField(persistent, "upscale_images")
                    if persistent.upscale_images:
                        textbutton _("Avoid Dialog") action ToggleField(persistent, "upscale_images_protect_dialog")
                        null height 10
                        text _("Minimum Size ([persistent.upscale_minimum_size])")
                        bar value FieldValue(persistent, 'upscale_minimum_size', 1000) xmaximum 300
                        text _("Maximum Size ([persistent.upscale_maximum_size])")
                        bar value FieldValue(persistent, 'upscale_maximum_size', 1000) xmaximum 300

                vbox:
                    style_prefix "radio"
                    label _("Movement")
                    textbutton _("Use Button Movement") action SetField(persistent, "movement", "button")
                    textbutton _("Use Portrait Movement") action SetField(persistent, "movement", "portrait")
                    textbutton _("Use List Movement") action SetField(persistent, "movement", "list")

                vbox:
                    style_prefix "check"
                    label _("Other")
                    text _("History Size ([persistent.history_size])")
                    text _("(Can severely slow down the game)") size 14
                    bar value FieldValue(persistent, 'history_size', 99, offset = 1) xmaximum 300
                    null height 10
                    textbutton _("Show Items on Top Bar") action ToggleField(persistent, "show_items_on_top_bar")


            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:
                    if config.has_music:
                        label _("Music & Video Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action [Preference("all mute", "toggle"), Preference("music volume", 1.0 if preferences.volumes['music'] == 0.0 else 0.0)]
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 450

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style check_text is gui_text

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        vbox:
            for h in _history_list:

                window:
                    ## This lays things out properly if history_height is None.
                    has fixed:
                        yfit True

                    if h.who:

                        label h.who:
                            style "history_name"

                            ## Take the color of the who text from the Character, if
                            ## set.
                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                    text h.what

        if not _history_list:
            label _("The dialogue history is empty.")


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## http://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    key 'K_RETURN' action yes_action
    key 'K_KP_ENTER' action yes_action

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        xpadding 40
        ypadding 40

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes(Enter)") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 45
    style_prefix "notify"

    frame at notify_appear:
      xpos 472
      ypos 90
      left_padding 10
      right_padding 15
      ypadding 10
      text message line_leading 5 outlines [ (1, "#000", 0, 0) ]

    timer persistent.notify_on_screen_time action Hide('notify')

transform notify_appear:
  on show:
      alpha 0.0
      linear 0.25 alpha 1.0

  on hide:
      linear 0.25 alpha 0.0
      function notify_transform


style notify_frame is default
style notify_text is gui_text

style notify_frame:
    background Frame("gui/notify.png", gui.notify_frame_borders)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## http://www.renpy.org/doc/html/screen_special.html#nvl

## note: colour of nvl.png is #934742


screen nvl(dialogue, items=None):
    zorder 2
    window:
        style "nvl_window"
        yanchor nvl_y_anchor

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    on 'show' action SetVariable('nvl_y_anchor', 0.0)


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id
            xsize 990

            fixed:
                xfit True
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    justify True
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xpos 480
    ypos 80
    background Frame("gui/nvl.png", gui.nvl_borders)
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    size 26
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 600

################################################################################
## Show Package Selection
################################################################################

screen package_select(packages = None):
    tag package_select

    add 'gui/bg/package_select.jpg'

    frame:
        style 'empty'
        padding (10, 10)
        frame:
            padding (20, 20)
            vbox:
                spacing 5
                label "Select Packages:" style "action_text"
                if len(package_actions) > 0:
                    text "\n".join(package_actions) size 20

                vpgrid:
                    xfill True
                    cols 3
                    spacing 5
                    mousewheel True
                    ymaximum 910

                    for package in packages:
                        button:
                            action (ToggleField(object=package, field='active', true_value=True, false_value=False), Jump(label='package_selection'))
                            hovered(Show('tooltip', s = "{b}Author:{/b} " + package.author + "\n{b}Description:{/b} " + package.description + "\n{b}Contains:{/b} " + ", ".join([pl[0] if pl[2] is None else pl[2] for pl in package.pregame_labels]) + "\n{b}Dependencies:{/b} " + (", ".join(package.dependencies) if package.dependencies else "None") + "\n{b}Conflicts:{/b} " + (", ".join(package.conflicts) if package.conflicts else "None") , tooltip_xanchor = 0.0))
                            unhovered(Hide('tooltip'))
                            hbox:
                                spacing 5
                                add ("#E0A366" if package.active else "#8C5E58") size (8,25)
                                text package.full_name style "action_text" hover_color "#D5C8B4"

                    for filler in range(3 - (len(packages) % 3)):
                        null

                frame:
                    xalign 0.99
                    textbutton "Accept" action Jump(label='after_package_selection') text_color "#FFF" text_hover_color "#D5C8B4"

################################################################################
## STATIC UI
################################################################################
style header_text:
    font 'fonts/JosefinSans-Regular.ttf'
    color '#000'
    size 21
    yalign 0.6

style title_text:
    font 'fonts/SpecialElite-Regular.ttf'
    color "#993300"
    size 33
    xalign 0.5

style small_text is gui_text:
    font 'fonts/JosefinSans-Regular.ttf'
    size 25

style tooltip_text is gui_text:
    font 'fonts/JosefinSans-Light.ttf'
    size 25

transform at_tooltip:
  function mouse_position
  pause 0.02
  repeat

screen tooltip(s, new_context = None, tooltip_xanchor = 0.5):
    zorder 5

    if new_context not in current_contexts_list:
        frame:
            style_prefix 'tooltip'
            top_padding 10
            xpadding 10
            xanchor tooltip_xanchor
            xmaximum 600
            at at_tooltip
            text s yalign 0.8

init python:
    y_adj = ui.adjustment()

style connection_button is empty
style connection_button:
    hover_background "#81534F88"

screen wt_static_ui:
    zorder 3

    key 'K_F5' action QuickSave()
    key 'K_F9' action QuickLoad()

    #TOP BAR
    fixed:
        style_prefix 'header'
        ymaximum 80
        # Resouces left side
        hbox:
            xpos 10
            xsize 480
            ysize 80
            for resource in [('week', 'CALENDAR', 145, "WEEK [week]  {} ".format(days[day].upper())), ('money', 'MONEY', 95, '[player.money]'), ('energy', "ENERGY", 70, '[player.energy]%')]:
                hbox:
                    spacing 8
                    if resource[0] != 'week':
                        button:
                            xsize 50
                            ysize 50
                            action NullAction()
                            add im.Scale("gui/button/{}.png".format(resource[0]), 50, 50)
                            hovered(Show('tooltip', s = resource[1], tooltip_xanchor = 0.0))
                            unhovered(Hide('tooltip'))
                    else:
                        imagebutton:
                            xsize 65
                            ysize 65
                            sensitive not running_scene
                            action (ToggleScreen('calendar', transition = Dissolve(0.2)), Call('reset_menu'))
                            auto "gui/button/calendar_%s.png".format(resource[0])
                            hovered(Show('tooltip', s = resource[1], tooltip_xanchor = 0.0))
                            unhovered(Hide('tooltip'))
                        null width 1

                    fixed:
                        xmaximum resource[2]
                        text resource[3] yalign 0.35

        # Actions (Player + Locations)
        viewport:
            style 'empty'
            xalign 1.0
            xmaximum 1430
            xfill False
            ysize 80
            mousewheel "horizontal"
            draggable True
            scrollbars "horizontal"

            frame:
                background None
                padding (0,5,10,0)
                $ actual_buttons = sorted([button for button in player.buttons if button.eval_action()] + [button for button in current_location.buttons if not button.new_context.endswith('_connection') or persistent.movement == 'button'], key=lambda button: button.button_weight)
                $ player_items = [i for i in player.items if i.has_portrait_image] if persistent.show_items_on_top_bar else []
                grid len(player_items + actual_buttons) 1:
                    xalign 1.0
                    spacing 5
                    # Player and location header buttons
                    for b in player_items + actual_buttons:
                        if isinstance(b, UISpace):
                            null width b.value xalign 0.5 yalign 0.5
                        elif isinstance(b, Action):
                            if b.use_owner_portrait:
                                button:
                                    xsize 64
                                    ysize 64
                                    focus_mask None
                                    sensitive  b.allow_button_on_scene or not running_scene
                                    action (SensitiveIf(not running_scene), Hide('tooltip'), SetVariable('action', b), Return())
                                    alternate (SensitiveIf(not running_scene), Hide('tooltip'), SetVariable('action', b.owner.examine_action), Return())
                                    hovered(Function(b.make_seen), Show('tooltip', s = b.owner.name, new_context = b.new_context, tooltip_xanchor = 1.0))
                                    unhovered(Hide('tooltip'))
                                    if b.owner.has_portrait_image and b.owner.cut_portrait:
                                        if b.allow_button_on_scene or not running_scene:
                                            background im.AlphaMask(renpy.displayable(b.owner.portrait), 'gui/button/alpha_portrait.png')
                                        else:
                                            background im.AlphaMask(im.MatrixColor(renpy.displayable(b.owner.portrait), im.matrix.desaturate()), 'gui/button/alpha_portrait.png')
                                    elif b.owner.has_portrait_image:
                                        if b.allow_button_on_scene or not running_scene:
                                            background b.owner.portrait
                                        else:
                                            background im.Grayscale(renpy.displayable(b.owner.portrait))
                                    else:
                                        if b.allow_button_on_scene or not running_scene:
                                            background im.MatrixColor('gui/button/alpha_portrait.png', im.matrix.colorize("#F58", "#FFF"))
                                        else:
                                            background im.MatrixColor('gui/button/alpha_portrait.png', im.matrix.colorize("#888", "#FFF"))
                                    add AlphaMask(Solid(color = "#000"), 'gui/button/alpha_border_portrait.png') pos(-4,-4) size(60,60)
                                    if b.is_unseen:
                                        foreground Image('gui/button/unseen.png', xalign = 1.0, yalign = 1.0)
                            else:
                                imagebutton:
                                    ypos -3
                                    xsize 64
                                    ysize 64
                                    auto b.auto_image
                                    if hasattr(player, 'inventory_action') and player.inventory_action == b:
                                        sensitive len(player.items) > 0 and (b.allow_button_on_scene or not running_scene) and b.eval_action()
                                    else:
                                        sensitive (b.allow_button_on_scene or not running_scene) and b.eval_action()
                                    action (Hide('tooltip'), SetVariable('action', b), Return())
                                    hovered(Function(b.make_seen), Show('tooltip', s =  b.evaled_name, new_context = b.new_context, tooltip_xanchor = 1.0))
                                    unhovered(Hide('tooltip'))
                                    if b.is_unseen:
                                        foreground Image('gui/button/unseen.png', xalign = 1.0, yalign = 1.0)

                        elif isinstance(b, Item):
                            button:
                                style 'empty'
                                xsize 60
                                ysize 60
                                focus_mask None
                                sensitive not running_scene
                                action (Hide('tooltip'), SetVariable('action', b), Return())
                                alternate (SensitiveIf(not running_scene), Hide('tooltip'), SetVariable('action', b.examine_action), Return())
                                hovered(Show('tooltip', s = b.name, new_context =  b.short_name + "_top_menu", tooltip_xanchor = 1.0))
                                unhovered(Hide('tooltip'))
                                add ConditionSwitch(b.cut_portrait, im.AlphaMask(renpy.displayable(b.portrait), 'gui/button/alpha_portrait.png'), "True", b.portrait) size(56, 56) pos (2,2)
                                add AlphaMask(Solid(color = "#000"), 'gui/button/alpha_border_portrait.png')
                                if b.is_unseen:
                                    foreground Image('gui/button/unseen.png', xalign = 1.0, yalign = 1.0)
                        else:
                            null


    #LEFT COLUMN (TITLE, HISTORY)
    frame:
        background None
        padding(0,0,0,0)
        yalign 1.0
        xsize 480
        ysize 1000

        vbox:
            spacing 10
            null height 8
            text "The Wifetrainer Files" style "title_text" xalign 0.3

            side "c l":
                xpos -5
                spacing 10

                viewport id 'history':
                    yadjustment y_adj
                    mousewheel True
                    draggable True
                    yinitial 1.0
                    arrowkeys True
                    pagekeys True

                    frame:
                        background None
                        padding(0,0,0,0)
                        yminimum 920
                        right_padding 10
                        bottom_padding 20

                        vbox:
                          yalign 1.0
                          xfill True
                          style_prefix 'small'
                          for h in _history_list[-persistent.history_size:]:
                            null height 15
                            if h.who:
                              text h.who: # a shadow. Probably.:
                                # outlines [ (1.5, "#000", 1.5, 1.5) ]
                                if "color" in h.who_args:
                                    color h.who_args["color"]

                            text h.what:
                              color "#000"
                              justify True
                              min_width 410
                              if "font" in h.what_args:
                                  font h.what_args["font"]
                              if not h.who:
                                  size 22

                vbar value YScrollValue('history') unscrollable "hide"

    # RIGHT COLUMN (People and Items)
    if persistent.movement == 'list':
        viewport:
            style 'empty'
            xpos 1510
            ypos 85
            xfill False
            yfill False
            xmaximum 420
            ymaximum 200
            mousewheel "vertical"
            draggable True
            scrollbars "vertical"

            hbox:
                box_wrap True
                box_wrap_spacing 5
                spacing 5
                xsize 400
                if current_location is not None:
                    for connection in current_location.get_menu_objects(current_location.short_name + "_connection"):
                        $ location = connection.location
                        button:
                            style 'empty'
                            background Frame("gui/frame.png", gui.frame_borders)
                            padding (5, 0)
                            ysize 35
                            xsize 195
                            action (SensitiveIf(not running_scene), Hide('tooltip'), SetVariable('action', connection), Return())
                            hovered (If(connection.costs_to_words != '',  Show('tooltip', s = connection.costs_to_words, tooltip_xanchor = 1.0), NullAction()))
                            unhovered (Hide('tooltip'))
                            hbox:
                                xalign 0.5
                                yalign 0.75
                                spacing 5
                                text (connection.name if connection.name is not None else location.name) size (18 if len(connection.name if connection.name is not None else location.name) > 14 else 24) hover_color '#E0A366'
                                if connection.is_unseen:
                                    add 'gui/button/unseen.png' yalign 0.2


    if persistent.movement == 'portrait':
        viewport:
            style 'empty'
            xpos 1510
            ypos 85
            xfill False
            yfill False
            xmaximum 420
            ymaximum 330
            mousewheel "vertical"
            draggable True
            scrollbars "vertical"

            hbox:
                box_wrap True
                spacing 5
                xsize 400
                if current_location is not None:
                    for connection in current_location.get_menu_objects(current_location.short_name + "_connection"):
                        $ location = connection.location
                        button:
                            style_prefix 'connection'
                            ysize 65
                            xsize 195
                            action (SensitiveIf(not running_scene), Hide('tooltip'), SetVariable('action', connection), Return())
                            hovered (If(connection.costs_to_words != '',  Show('tooltip', s = connection.costs_to_words, tooltip_xanchor = 1.0), NullAction()))
                            unhovered (Hide('tooltip'))
                            hbox:
                                spacing 5
                                yalign 0.5
                                frame:
                                    style 'empty'
                                    xsize 60
                                    ysize 60
                                    if location.has_portrait_image and location.cut_portrait:
                                        if not running_scene:
                                            background im.AlphaMask(renpy.displayable(location.portrait), 'gui/button/alpha_portrait.png')
                                        else:
                                            background im.AlphaMask(im.Grayscale(renpy.displayable(location.portrait)), 'gui/button/alpha_portrait.png')
                                    elif location.has_portrait_image:
                                        if not running_scene:
                                            background location.portrait
                                        else:
                                            background im.Grayscale(renpy.displayable(location.portrait))
                                    else:
                                        if not running_scene:
                                            background im.MatrixColor('gui/button/alpha_portrait.png', im.matrix.colorize("#F58", "#FFF"))
                                        else:
                                            background im.MatrixColor('gui/button/alpha_portrait.png', im.matrix.colorize("#888", "#FFF"))
                                    add im.MatrixColor('gui/button/alpha_border_portrait.png', im.matrix.colorize('#000', "#FFF")) size (61, 61)
                                    if connection.is_unseen:
                                        foreground Image('gui/button/unseen.png', xalign = 1.2, yalign = 1.1)
                                text (connection.name if connection.name is not None else location.name) size 20 yalign 0.5 color '#000' text_align 0.5

    viewport:
        xpos 1510
        ypos (420 if persistent.movement in ['portrait', 'list'] else 85)
        xfill False
        yfill False
        xmaximum 420
        ymaximum 195
        mousewheel "vertical"
        draggable True
        scrollbars "vertical"

        $ people_in_room = sorted(player.other_people_in_room, key=lambda p: p.name)
        $ items_in_room = sorted([i for i in current_location.items], key=lambda item: item.name)
        $ actual_button_num = len(people_in_room) + len(items_in_room)
        $ actual_rows = int(ceil((actual_button_num / 6.0)))
        grid 6 actual_rows:
            spacing 8
            # People in room
            for person in people_in_room:
                button:
                    xsize 60
                    ysize 60
                    focus_mask None
                    action (SensitiveIf(not running_scene), Hide('tooltip'), SetVariable('action', person), Return())
                    alternate (SensitiveIf(not running_scene), Hide('tooltip'), SetVariable('action', person.examine_action), Return())
                    hovered (Show('tooltip', s = person.name, new_context = person.short_name + "_top_menu", tooltip_xanchor = 1.0))
                    unhovered (Hide('tooltip'))
                    if person.has_portrait_image and person.cut_portrait:
                        if not running_scene:
                            background im.AlphaMask(renpy.displayable(person.portrait), 'gui/button/alpha_portrait.png')
                        else:
                            background im.AlphaMask(im.Grayscale(renpy.displayable(person.portrait)), 'gui/button/alpha_portrait.png')
                    elif person.has_portrait_image:
                        if not running_scene:
                            background person.portrait
                        else:
                            background im.Grayscale(renpy.displayable(person.portrait))
                    else:
                        if not running_scene:
                            background im.MatrixColor('gui/button/alpha_portrait.png', im.matrix.colorize("#F58", "#FFF"))
                        else:
                            background im.MatrixColor('gui/button/alpha_portrait.png', im.matrix.colorize("#888", "#FFF"))
                    add im.MatrixColor('gui/button/alpha_border_portrait.png', im.matrix.colorize(Color(person.c.who_args['color']), "#FFF")) pos(-4, -4)
                    if person.is_unseen:
                        foreground Image('gui/button/unseen.png', xalign = 1.0, yalign = 1.0)

            # Items in the room
            for item in items_in_room:
                button:
                    xsize 60
                    ysize 60
                    focus_mask None
                    action (SensitiveIf(not running_scene), Hide('tooltip'), SetVariable('action', item), Return())

                    hovered(Show('tooltip', s = item.name, new_context = item.short_name + "_top_menu", tooltip_xanchor = 1.0))
                    unhovered(Hide('tooltip'))
                    if item.has_portrait_image and item.cut_portrait:
                        if not running_scene:
                            background im.AlphaMask(renpy.displayable(item.portrait), 'gui/button/alpha_portrait.png')
                        else:
                            background im.AlphaMask(im.Grayscale(renpy.displayable(item.portrait)), 'gui/button/alpha_portrait.png')
                    elif item.has_portrait_image:
                        if not running_scene:
                            background item.portrait
                        else:
                            background im.Grayscale(renpy.displayable(item.portrait))
                    else:
                        if not running_scene:
                            background im.MatrixColor('gui/button/alpha_portrait.png', im.matrix.colorize("#F58", "#FFF"))
                        else:
                            background im.MatrixColor('gui/button/alpha_portrait.png', im.matrix.colorize("#888", "#FFF"))
                    add 'gui/button/alpha_border_portrait.png' pos(-4, -4)
                    if item.is_unseen:
                        foreground Image('gui/button/unseen.png', xalign = 1.0, yalign = 1.0)

            for space in xrange(0, actual_rows * 6 - actual_button_num):
                null


style overlay_text is text:
    kerning -5
    size 60
    color gui.overlay_text_color

screen static_background:
    zorder 0

    button:
      xsize 0
      ysize 0
      action (ToggleVariable('say_y_anchor', 1.0, 2.0), ToggleVariable('nvl_y_anchor', 0.0, 2.0))
      alternate (ToggleVariable('say_y_anchor', 1.0, 2.0), ToggleVariable('nvl_y_anchor', 0.0, 2.0))
      keysym 'h'
      alternate_keysym 'mouseup_2'

    frame:
        xfill True
        yfill True
        background "#D5C8B4"

    add player.bg:
        xanchor 1.0
        yalign 1.0
        xpos 1920

    fixed:
        style_prefix 'overlay'
        xmaximum 420
        ymaximum 200
        xalign 1.0
        ypos (436 if persistent.movement in ['portrait', 'list'] else 230)

        if current_location:
            text current_location.name.upper():
                xalign 1.0
                yalign 1.0
                text_align 1.0


    text "CHOICES":
        style_prefix 'overlay'
        xalign 1.0
        yanchor 1.0
        ypos 1094

    # Right Colum Separator Line
    if persistent.movement in ['portrait', 'list']:
        add Solid(gui.border_color):
            size(420, 1)
            xalign 1.0
            ypos 413

    add Solid(gui.border_color):
        size(420, 1)
        xalign 1.0
        ypos (621 if persistent.movement in ['portrait', 'list'] else 415)

    # Separator Line
    add Solid(gui.border_color):
        size(1920, 1)
        ypos 71

    # Vertical Lines
    add Solid(gui.border_color):
        size(1, 1020)
        xpos 471
        ypos 72

    add Solid(gui.border_color):
        size(1, 1020)
        xpos 1490
        ypos 72

################################################################################
## Custom Say Dialog Window
################################################################################

style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style say_label:
    properties gui.text_properties("name", accent=True)

style say_dialogue:
    properties gui.text_properties("dialogue")

screen say(who, what):
    zorder 3
    frame id 'window':
        background gui.dialogue_background_default_color  ## the last two digits sets the alpha percentage of transparency for the backdrop to the dialogue text box
        xanchor 0.0
        yalign say_y_anchor
        xpos 471
        xsize 1020
        ysize 200
        top_padding 15
        xpadding 15

        viewport:
            mousewheel True
            scrollbars "vertical"
            xsize 1020
            ysize 200
            hbox:
                spacing 10
                if who is not None:
                    # text who id 'who' outlines [ (2, "#000", 1, 1) ] xmaximum 200 yalign 0.5# a shadow. Probably.
                    text who id 'who' xmaximum 200 yalign 0.5# a shadow. Probably.
                    add im.Scale('gui/bar/bottom.png', 3, 180) yalign 0.5
                text what id 'what'

    on 'show' action (SetVariable('say_y_anchor', 1.0), SetVariable('break_advance_time', True), Hide('advance_time'), Hide('calendar'))

################################################################################
## Custom Choice Menus
################################################################################

## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True

style choice_button is frame:
    background None
    padding (5, 5)

style choice_text is gui_text:
    color "#FFF"
    hover_color "#000"

style choice_button_text is choice_text:
    font 'fonts/JosefinSans-Regular.ttf'
    size 22
    hover_color "#d5c8b4"

screen choice(items):
    default screen_title = action.evaled_var('title') if title is None and action is not None and 'title' in action.__dict__ else title
    modal True

    zorder 4
    style_prefix "choice"

    on "replace" action If(preferences.mouse_move, MouseMove(x=1550, y=475))

    frame:
        ypadding 20
        xpadding 20
        xanchor 1.0
        yanchor 0.0
        xpos 1916
        ypos (625 if persistent.movement in ['portrait', 'list'] else 420)
        xsize 410

        vbox:
            if screen_title is not None:
                text screen_title size 26:
                    xalign 0.5
                    text_align 0.5
            # Separator Line
            add Solid(gui.border_color):
                size(300 ,3)
                align(0.5, 0.5)

            null height 10

            viewport:
                style 'empty'
                xsize 372
                yfill False
                ymaximum (360 if persistent.movement in ['portrait', 'list'] else 565)
                mousewheel "vertical"
                edgescroll (30, 1000)
                scrollbars "vertical"
                vbox:
                    xsize 352
                    spacing 10

                    for i in items:
                        textbutton i.caption:
                            action (i.action, Function(add_to_history, s = screen_title), Function(add_to_history, s = i.caption))

################################################################################
## Actions Menu
################################################################################

init python:
  def mouse_position(trans, st, at):
    x, y = renpy.get_mouse_pos()
    trans.xpos = x
    trans.ypos = y

transform position_at_mouse:
  function mouse_position

style actions_text is small_text
style actions_button_text is small_text:
    hover_color "#d5c8b4"

screen menu_holder_0(menu_position, menu_context, is_item_menu):
    zorder 10
    style_prefix 'actions'
    use actions_menu(menu_position, menu_context, is_item_menu, 'menu_holder_0')

    if menu_shown and not renpy.get_screen('menu_holder_modal'):
        button:
            xsize 0
            ysize 0
            action (Show('menu_holder_afterimage'), Call('hide_menu', mark_menu_as_hidden = False))
            alternate (Show('menu_holder_afterimage'), Call('hide_menu', mark_menu_as_hidden = False))
            keysym 'h'
            alternate_keysym 'mouseup_2'

screen menu_holder_1(menu_position, menu_context, is_item_menu):
    zorder 11
    style_prefix 'actions'
    use actions_menu(menu_position, menu_context, is_item_menu, 'menu_holder_1')

screen menu_holder_2(menu_position, menu_context, is_item_menu):
    zorder 12
    style_prefix 'actions'
    use actions_menu(menu_position, menu_context, is_item_menu, 'menu_holder_2')

screen menu_holder_3(menu_position, menu_context, is_item_menu):
    zorder 13
    style_prefix 'actions'
    use actions_menu(menu_position, menu_context, is_item_menu, 'menu_holder_3')

screen menu_holder_4(menu_position, menu_context, is_item_menu):
    zorder 14
    style_prefix 'actions'
    use actions_menu(menu_position, menu_context, is_item_menu, 'menu_holder_4')

screen menu_holder_5(menu_position, menu_context, is_item_menu):
    zorder 15
    style_prefix 'actions'
    use actions_menu(menu_position, menu_context, is_item_menu, 'menu_holder_5')

screen menu_holder_modal(menu_position, menu_context, is_item_menu):
    zorder 16
    modal True
    style_prefix 'actions'

    if menu_shown:
        button:
            xsize 0
            ysize 0
            action (Show('menu_holder_modal_afterimage'), Call('hide_menu', mark_menu_as_hidden = False))
            alternate (Show('menu_holder_modal_afterimage'), Call('hide_menu', mark_menu_as_hidden = False))
            keysym 'h'
            alternate_keysym 'mouseup_2'

    use actions_menu(menu_position, menu_context, is_item_menu, 'menu_holder_modal')

screen menu_holder_modal_afterimage:
    zorder 90
    modal True

    button:
        xsize 1920
        ysize 1080
        focus_mask None
        action (Hide('menu_holder_modal_afterimage'), Call('show_menu'))
        alternate (Hide('menu_holder_modal_afterimage'), Call('show_menu'))
        keysym 'h'
        alternate_keysym 'mouseup_2'

screen menu_holder_afterimage:
    zorder 90
    modal False

    button:
        xsize 1920
        ysize 1080
        focus_mask None
        action (Hide('menu_holder_afterimage'), Call('show_menu'))
        alternate (Hide('menu_holder_afterimage'), Call('show_menu'))
        keysym 'h'
        alternate_keysym 'mouseup_2'


style action_menu_button is empty
style action_menu_button:
    hover_background "#993300"

screen actions_menu(menu_position, menu_context, is_item_menu, parent_menu):
    style_prefix "action_menu"
    if is_item_menu:
        if menu_context == 'inventory':
            $ item_list = player.items
        elif menu_context == 'location_items':
            $ item_list = current_location.items
        elif menu_context == 'store':
            $ item_list =  current_store.store_items
        else:
            $ item_list = []

        if len(item_list) > 0:
            button:
                style 'empty'
                action NullAction()
                xanchor 1.0
                pos menu_position
                frame:
                    padding (20, 20)
                    if 'store' in current_contexts_list and isinstance(item_list, list):
                        hbox:
                            vbox:
                                frame:
                                    ysize 30
                                    background None
                                    padding (0,0,10,0)
                                    text "ITEM" yalign 0.5 size 27
                                for i in [item for item in item_list if item.available_quantity != 0]:
                                    button:
                                        action (SetVariable('action', i), Return()) yalign 0.5 focus_mask None ysize 30
                                        size_group menu_context
                                        text i.item.name + ("(x{})".format(i.single_buy_amount) if i.single_buy_amount > 1 else "") color "#FFF" size 26

                            vbox:
                                frame:
                                    ysize 30
                                    xsize 100
                                    background None
                                    padding (0,0,10,0)
                                    text "QTY" xalign 1.0 yalign 0.5 size 27
                                    null height 3
                                for i in [item for item in item_list if item.available_quantity != 0]:
                                    frame:
                                        ysize 30
                                        xsize 100
                                        background None
                                        padding (0,0)
                                        text "{}".format(i.available_quantity if i.available_quantity > 0 else "∞") xalign 1.0 yalign 0.5

                            vbox:
                                frame:
                                    ysize 30
                                    xsize 100
                                    background None
                                    padding (0,0,10,0)
                                    text "PRICE" xalign 1.0 yalign 0.5 size 27
                                    null height 3
                                for i in [item for item in item_list if item.available_quantity != 0]:
                                    frame:
                                        ysize 30
                                        xsize 100
                                        background None
                                        padding (0,0,10,0)
                                        text "{}".format(i.final_price()) xalign 1.0 yalign 0.5

                    else:
                        hbox:
                            xmaximum 980
                            box_wrap True
                            box_wrap_spacing 20
                            spacing 20
                            xalign 0.0
                            if isinstance(item_list, ItemDict):
                                for item in item_list.keys():
                                    button:
                                        action (SensitiveIf(get_non_empty_actions(item.get_menu_objects("_top_menu")) != []), SetVariable('action', item), Return())
                                        alternate (SetVariable('action', item.examine_action), Return())
                                        size_group menu_context
                                        hbox:
                                            first_spacing 10
                                            spacing 20
                                            frame:
                                                style 'empty'
                                                xsize 60
                                                ysize 60
                                                if item.has_portrait_image and item.cut_portrait:
                                                    if not running_scene:
                                                        background im.AlphaMask(renpy.displayable(item.portrait), 'gui/button/alpha_portrait.png')
                                                    else:
                                                        background im.AlphaMask(im.Grayscale(renpy.displayable(item.portrait)), 'gui/button/alpha_portrait.png')
                                                elif item.has_portrait_image:
                                                    if not running_scene:
                                                        background item.portrait
                                                    else:
                                                        background im.Grayscale(renpy.displayable(item.portrait))
                                                else:
                                                    if not running_scene:
                                                        background im.MatrixColor('gui/button/alpha_portrait.png', im.matrix.colorize("#F58", "#FFF"))
                                                    else:
                                                        background im.MatrixColor('gui/button/alpha_portrait.png', im.matrix.colorize("#888", "#FFF"))
                                                add 'gui/button/alpha_border_portrait.png' size(64,64) pos(-1, -1)
                                                if item.is_unseen:
                                                    foreground Image('gui/button/unseen.png', xalign = 1.0, yalign = 1.0)

                                            fixed:
                                                xsize 150
                                                ysize 60
                                                text item.name color "#FFF" size 26 yalign 0.5

                                            fixed:
                                                xsize 60
                                                ysize 60
                                                text "{}".format(item_list[item]) xalign 1.0 yalign 0.6

    else:
        $ menu_objects = current_target.get_menu_objects(menu_context)
        if len(get_non_empty_actions(menu_objects)) > 0:
            frame:
                xanchor 1.0
                pos menu_position

                vbox:
                    for a in get_non_empty_actions(menu_objects):
                        if isinstance(a, Action):
                            if isinstance(a, WTText):
                                text a.name
                            else:
                                if a.is_zero_charge():
                                    button:
                                        action (SetVariable('action', a), Return())
                                        hovered Function(a.make_seen)
                                        size_group parent_menu
                                        padding (5,5)
                                        hbox:
                                            spacing 5
                                            text a.evaled_name size 26
                                            if a.is_unseen:
                                                add 'gui/button/unseen.png' size(20, 20) align(0.5, 0.5) yoffset -1
                                            if a.ends_day_icon:
                                                add 'gui/button/end_day.png' size(20, 20) align(0.5, 0.5)
                                else:
                                    button:
                                        action (SetVariable('action', a), Return())
                                        hovered Function(a.make_seen)
                                        size_group parent_menu
                                        padding (5,5)
                                        hbox:
                                            spacing 5
                                            text "{} ({})".format(a.evaled_name, a.costs_to_words) size 26
                                            if a.is_unseen:
                                                add 'gui/button/unseen.png' size(20, 20) align(0.5, 0.5) yoffset -1
                                            if a.ends_day_icon:
                                                add 'gui/button/end_day.png' size(20, 20) align(0.5, 0.5)

################################################################################
## Show WT images
################################################################################

screen trainee_image(ti, w, h, is_video):
    zorder 1
    tag trainee_image

    if is_video:
        if persistent.upscale_images:
            add ti anchor (0.5, 0.0) pos (981, 76) maxsize(min(persistent.upscale_maximum_size, max(w, persistent.upscale_minimum_size)), min(persistent.upscale_maximum_size, max(h, persistent.upscale_minimum_size)))
        else:
            add ti anchor (0.5, 0.0) pos (981, 76) maxsize(1000, 1000)
    elif persistent.upscale_images:
        add ti anchor (0.5, 0.0) pos (981, 76) maxsize(min(persistent.upscale_maximum_size, max(w, persistent.upscale_minimum_size)), min(min(800, persistent.upscale_maximum_size) if persistent.upscale_images_protect_dialog else persistent.upscale_maximum_size, max(h, persistent.upscale_minimum_size)))
    else:
        add ti anchor (0.5, 0.0) pos (981, 76) maxsize(min(1000, w), min(1000, h))

################################################################################
## BLACK VOODOO MAGIC UI
################################################################################

screen wait_for_input:
    zorder 2

    button:
        xsize 1920
        ysize 1080
        action (SetVariable('action', empty_action), Return())
        #at cycle_check_button_trees

################################################################################
## CALENDAR
################################################################################

style calendar_text is gui_text:
    color "#000"

style calendar_active_text is gui_text:
    color "#FFF"

style calendar_notes_text is calendar_text:
    size 25

style calendar_notes_active_text is calendar_active_text:
    size 25

screen calendar():
    style_prefix 'calendar'
    tag calendar
    zorder 4

    button:
      xsize 1920
      ysize 1080
      background "#00000088"
      action (Hide('calendar'), Call('reset_menu'))

    vbox:
        xalign 0.5
        yalign 0.5

        frame:
            background Frame("gui/calendar/square_big.png", Borders(4, 4, 4, 4))
            hbox:
                frame:
                    xsize 50
                    ysize 50
                    background Frame("gui/calendar/square.png", Borders(2, 2, 2, 2))
                for i in xrange(0, 5):
                    frame:
                        xsize 290
                        ysize 50
                        background Frame("gui/calendar/square.png", Borders(2, 2, 2, 2))
                        text days[i+1] color "#000" xalign 0.5 yalign 0.5

        frame:
            background Frame("gui/calendar/square_big.png", Borders(4, 4, 4, 4))
            viewport id 'calendar':
                xsize 1500
                ysize 1000
                draggable True
                mousewheel True
                hbox:
                  vbox:
                    for i in get_calendar_range_weeks():
                      frame:
                        xsize 55
                        ysize 200
                        background Frame("gui/calendar/square.png", Borders(2, 2, 2, 2))
                        text "WEEK-"+str(i)  vertical True size 24 xalign 0.5 yalign 0.5
                  grid 5 30:
                      for i in get_calendar_range_days():
                          button:
                              action Call('add_calendar_actions', clicked_day = i)
                              xsize 290
                              ysize 200
                              if total_days == i:
                                  style_prefix 'calendar_active'
                                  background Frame("gui/calendar/square_active.png", Borders(2, 2, 2, 2))
                              else:
                                  background Frame("gui/calendar/square.png", Borders(2, 2, 2, 2))
                              text str(i) xalign 1.0 yalign 1.0
                              frame:
                                  background None
                                  if total_days == i:
                                      style_prefix 'calendar_notes_active'
                                  else:
                                      style_prefix 'calendar_notes'

                                  vbox:
                                      for note in get_notes(i):
                                          text '- ' + note

screen advance_time:
    zorder 100
    modal True

    frame:
      xfill True
      yfill True
      background "#00000088"

      frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 50
        text "Advancing Time..." size 40

################################################################################
## OTHER SCREENS
################################################################################
style content_advisory_grid_text is gui_text:
    size 20

screen content_advisory():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Content Advisory Warning")):

        vbox:
            xpos 130
            ypos 50
            xsize 1380
            spacing 30

            text _('To play this game, you must be of legal age to view pornography in your jurisdiction.')
            text _("The core of this game is 'normal' male-female sex acts. Typically the man is in the initiating role and the woman a consenting adult.  There are also story lines that lead to a variety of other sexual activities, some of which you may find offensive. Some of the options the game allows you to explore (generally from most content to least) are:")
            grid 2 11:
                style_prefix 'content_advisory_grid'
                xspacing 60
                yspacing 10
                text _("Oral sex (both MF and FM)")
                text _("Intercourse")
                text _("Anal sex (mostly MF)")
                text _("Hand jobs, foot jobs, tit jobs and the like")
                text _("Domination and submission\n(usually M/f but with some F/f and F/m, including pain play)")
                text _("Mind control (though hypnosis and magic)")
                text _("Stripping and modelling")
                text _("Bi-sexuality and homosexuality (mostly FF but some MM)")
                text _("Objectification\n(usually F but also M, including puppy play, bimbo-fication and humiliation)")
                text _("Threesomes and group sex")
                text _("Pimping")
                text _("Exhibitionism")
                text _("Cuckolding (and some cuckquean)")
                text _("Living dolls")
                text _("Orgasm denial")
                text _("Financial domination")
                text _("Cum fetish")
                text _("Watersports")
                text _("Blackmail")
                text _("Age play by adults")
                text _("Incest (very little)")
                text _("Upskirt (very little)")
                #null
            text _("The actions that lead to these story lines are sufficiently described as to give you an understanding of the direction you are taking the characters. If you are uncomfortable with any of the above activities, simply do not choose the actions that lead to them (or delete this game from your computer).")

screen model_credits():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Model Credits")):

        $ full_list = [c[1] for c in model_credits if c[0] == 'full']
        $ full_count = len(full_list)

        $ sup_list = [c[1] for c in model_credits if c[0] == 'support']
        $ sup_count = len(sup_list)

        $ bits_list = [c[1] for c in model_credits if c[0] == 'bit']
        $ bits_count = len(bits_list)

        viewport:
            mousewheel True
            draggable True

            side_yfill True

            xpos 130
            ypos 50
            xsize 1380
            ysize 860

            vbox:
                spacing 30

                label "Major Clients:"
                grid 2 ceil(full_count / 2.0):
                    xspacing 50
                    transpose True

                    for c in full_list:
                        text _(c)

                    if full_count % 2 == 1:
                        null

                label "Supporting Characters:"
                grid 2 ceil(sup_count / 2.0):
                    transpose True
                    xspacing 50

                    for c in sup_list:
                        text _(c)

                    if sup_count % 2 == 1:
                        null

                label "Bit Parts:"
                grid 3 ceil(bits_count / 3.0):
                    style_prefix 'content_advisory_grid'
                    xspacing 50
                    transpose True

                    for c in bits_list:
                        text _(c)

                    if bits_count % 3 == 1:
                        null
                        null

                    elif bits_count % 3 == 2:
                        null

screen warning:
  frame:
    xfill True
    yfill True
    xpadding 300
    ypadding 300
    background None

    vbox:
        xalign 0.5
        yalign 0.5

        text "WARNING" size 70 color "#F00" xalign 0.5
        null height 50

        text "This game contains adult material not suitable for viewing by minors.\nIt depicts graphic sexual situations, including some that are violent and unsafe and should not be attempted in real life." size 40 xalign 0.5 text_align 0.5
        null height 100

        vbox:
            xalign 0.5
            textbutton "Understood. I'm an adult and want to {color=#0A0}continue{/color}." action Return() background "#222"
            null height 30

            vbox:
                xalign 0.5
                textbutton "Understood. I want to {color=#A00}quit{/color}." action Quit(False) background "#222"

transform fade_in:
  on show:
    alpha 0.0
    linear 0.5 alpha 1.0

screen black_overlay:
    zorder 200

    frame at fade_in:
      xfill True
      yfill True

      background "#000"

style examine_button is empty

screen examine_self:
    modal True
    style_prefix 'examine'
    zorder 99
    button:
        action Hide('examine_self')
        frame:
            background "#00000000"
            xsize 1920
            ysize 1080
            frame:
                xpos 465
                ypos 67
                xsize 1010
                ysize 1000
                viewport:
                    mousewheel True
                    frame:
                        background None
                        padding (40, 25)
                        vbox:
                            text "You are a {b}[player.category_name]{/b}."
                            hbox:
                                first_spacing 10
                                text "Reputation: "
                                for i in range(player.reputation):
                                    add "gui/button/star.png" yoffset 2
                            null height 10
                            for phrase in [phrase for phrase in player.examine_phrases if phrase.eval_condition]:
                                text phrase.phrase

                            null height 10
                            text "{b}You have successfully:{/b}\nHypnotized [player.hypno_action_count] times\nSeduced [player.desire_action_count] times\nDominated [player.submission_action_count] times\nLowered a client's resistance [player.resistance_action_count] times\nIncreased a client's sense of self [player.sos_action_count] times"
                            if player.virgin_count == 1:
                                text "Deflowered 1 Virgin"
                            elif player.virgin_count > 1:
                                text "Deflowered [player.virgin_count] Virgins"
                            null height 10
                            # text "{b}You have created:{/b}\n[player.satisfied_client_count] Satisfied Clients\n[player.lesbian_count] Lesbians\n[player.domme_count] Dommes\n[player.showgirl_count] Showgirls\n[player.new_people_count] New People"
                            text "{b}You have created:{/b}\n[player.lesbian_count] Lesbians\n[player.domme_count] Dommes\n[player.showgirl_count] Showgirls"
                            null height 10
                            text "{b}You have:{/b}\n[player.girlfriend_count] Girlfriends and [player.hypno_girlfriend_count] Hypno-girlfriends\n[player.teaching_aide_count] Teaching Aides and [player.assistant_count] Hypnotist Assistants\n[player.whore_count] Working Girls and [player.bimbo_count] Bimbos\n[player.slavegirl_count] Slavegirls and [player.petgirl_count] Petgirls\n[player.doll_count] Dolls and [player.degraded_count] Degraded Girls\n[player.adult_baby_count] Adult Babies"
                            null height 10
                            text "{b}You have had:{/b}\n[player.handjob_count_total] Handjobs and [player.hypno_handjob_count_total] Handjobs during Hypnosis\n[player.blowjob_count_total] Blowjobs and [player.hypno_blowjob_count_total] Blowjobs during Hypnosis\n[player.titfuck_count_total] Titjobs and [player.hypno_titfuck_count_total] Titjobs during Hypnosis\n[player.sex_count_total] Vaginal Intercourse and [player.hypno_sex_count_total] Vaginal Intercourse during Hypnosis\n[player.anal_count_total] Anal Intercourse and [player.hypno_anal_count_total] Anal Intercourse during Hypnosis\n[player.swallow_count_total] Swallowed Finishes and [player.hypno_swallow_count_total] Swallowed Finishes during Hypnosis\n[player.facial_count_total] Facial Finishes and [player.hypno_facial_count_total] Facial Finishes during Hypnosis"

screen examine_alexis_memo:
    modal True
    style_prefix 'examine'
    zorder 99
    button:
        action Hide('examine_alexis_memo')
        frame:
            background "#00000000"
            xsize 1920
            ysize 1080
            frame:
                xpos 465
                ypos 67
                xsize 1010
                ysize 1000
                viewport:
                    mousewheel True
                    frame:
                        background None
                        padding (40, 25)
                        vbox:
                            # Memo Display
                            text "The memo is organized by Key Performance Indicators, the text punctuated by concise bullet points. You flip to the executive summary."
                            null height 20
                            text "{font=fonts/JosefinSans-Regular.ttf}{size=-5}{b}Compliance{/b} \n[alexis.compliant_text]{/size}{/font}"
                            #text "• {font=fonts/JosefinSans-Regular.ttf}{size=-5}{b}Compliance:{/b} \n[alexis.compliant_text]{/size}{/font}"
                            null height 20
                            text "{font=fonts/JosefinSans-Regular.ttf}{size=-5}{b}Obedience{/b} \n[alexis.obedient_text]{/size}{/font}"
                            #text "• {font=fonts/JosefinSans-Regular.ttf}{size=-5}{b}Obedience:{/b} \n[alexis.obedient_text]{/size}{/font}"
                            null height 20
                            text "{font=fonts/JosefinSans-Regular.ttf}{size=-5}{b}Role Acceptance{/b} \n[alexis.accepting_text]{/size}{/font}"
                            #text "• {font=fonts/JosefinSans-Regular.ttf}{size=-5}{b}Role Acceptance:{/b} \n[alexis.accepting_text]{/size}{/font}"
                            if alexis.sexual_skills_discussion >= 6:
                              null height 20
                              text "{font=fonts/JosefinSans-Regular.ttf}{size=-5}[alexis.sexual_skills_text]{/size}{/font}"
                              #text "• {font=fonts/JosefinSans-Regular.ttf}{size=-5}[alexis.sexual_skills_text]{/size}{/font}"
                            elif alexis.sexual_skills_discussion > 0:
                              null height 20
                              text "{font=fonts/JosefinSans-Regular.ttf}{size=-5}[alexis.sexual_skills_title_text]{/size}{/font}"
                              #text "• {font=fonts/JosefinSans-Regular.ttf}{size=-5}[alexis.sexual_skills_title_text]{/size}{/font}"
