register_package alternative_start name "Alternative Start" author "Digital Bonsai" description "Alternative Start Proof of Concept. Do not turn this on unless you are replacing Core." disabled conflicts core
register alternative_core_pregame 1 in alternative_start as "Alternative Start"

label alternative_core_pregame:

    # Add day labels
    day_label add to start core_start_day priority first
    day_label add to end core_end_day priority last

    python:
        # Player Object
        player = Player(Character("You", who_color = "#FFF"))
        player.add_tag('player')
        player.remove_tags_daily.add('used_energy')

        # Starting Location
        garage = Location("Garage", 'ga', area = 'house', unseen = False)
        garage.add_button("Your Phone", new_context = "_phone", condition = "garage.is_empty", auto_image = "gui/button/phone_%s.png")
        garage.add_action("Check Messages", context = '_phone', new_context = "_check_messages")
        garage.add_action("Arrange Session with Client", context = '_phone', new_context = "_call_clients", condition = "garage.is_empty and any_client(with_status = 'on_training') and not is_weekend()", ends_day_icon = True)

        # Needed locations cuz I'm lazy and I don't want to edit jasmine
        living_room = garage
        bedroom = Location("Bedroom" , 'be', cut_portrait = True, area = 'house', unseen = False)
        dungeon = Location("Dungeon", 'du', cut_portrait = True, submission_mod = 5, area = 'house', unseen = False)
        downtown = Location("Downtown", 'do', cut_portrait = True, area = 'downtown', unseen = False)

        # Current Location
        starting_location = garage
        current_location = garage
        last_location = garage
    return
