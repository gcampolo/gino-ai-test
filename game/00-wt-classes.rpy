# This is a python block that is invoked on 0 order (less is earlier)
init 0 python:
    # Packages
    from toposort import toposort_flatten, toposort
    from num2word_EN import to_card, to_ord, to_ordnum, to_year
    from math import ceil, floor
    from copy import deepcopy
    import collections
    import itertools
    import os

    ###
    # Renpy configs
    ###

    config.keymap['hide_windows'] = []

    ###
    # Versioning compatibility
    ###

    versions = { "core": ['0_7g', '0_7h', '0_7i', '0_7j', '0_7k', '0_7l', '0_7l2', '0_7l3', '0_7m', '0_7n', '0_7o', '0_7o2', '0_7p', '0_7q', '0_7r'] }

    ###
    # Loading images
    ###

    image_extensions = ('jpg', 'jpeg', 'png', 'webp',)
    video_extensions = ('webm',)

    for candidate in [file for file in renpy.list_files() if 'modules' in file and file.endswith(image_extensions + video_extensions)]:
        candidate_name = candidate.rsplit('.', 1)[0].rsplit('/', 1)[-1].replace(' ', '_').lower()

        if candidate.endswith(image_extensions):
            renpy.image(candidate_name, candidate)
        elif candidate.endswith(video_extensions):
            renpy.image(candidate_name + '_movie', Movie(channel = 'trainee', play = candidate))

    ###
    # Helpers Classes
    ###

    # Semi persistant
    # This class only job is to make information persist over restarts but not full restarts
    # No need to care about it unless you are doing some really weird stuff
    class Persist(renpy.store.object):
        def __init__(self):
            pass
    persist = Persist()

    # This class is used to add support for any method to int based stats
    # Currently it allows to write numbers into words in a format that Renpy understands like [current_target.resistance.to_s]
    class ext_int(int):
        def __new__(cls, value):
            return int.__new__(cls, value)

        def __add__(self, b):
            return ext_int(int(self) + b)

        def __sub__(self, b):
            return ext_int(int(self) - b)

        def __mul__(self, b):
            return ext_int(int(self) * b)

        def __div__(self, b):
            return ext_int(int(self) / b)

        def __radd__(self, b):
            return ext_int(int(self) + b)

        def __rsub__(self, b):
            return ext_int(b - int(self))

        def __rmul__(self, b):
            return ext_int(int(self) * b)

        def __rdiv__(self, b):
            return ext_int(b / int(self))

        def __pow__(self, b):
            return ext_int(pow(int(self), b))

        @property
        def to_s(self):
            return to_card(self)

        @property
        def to_o(self):
            return to_ord(self)

        @property
        def to_on(self):
            return to_ordnum(self)

        @property
        def to_y(self):
            return to_year(self)

    # This MutableSet will take care of changing location directly in person when required by Location changes.
    # No need to mess with it
    class PeopleSet(collections.MutableSet):
        def __init__(self, location, people = ()):
            self._location = location
            self._people_set = set()
            for p in people: self.add(p)

        def add(self, person):
            if person.location is not None:
                person.location.people.discard(person)

            self._people_set.add(person)
            person._location = self._location

        def discard(self, person):
            if person in self._people_set:
                person._location = None
                self._people_set.discard(person)

        def __iter__(self):
            return iter(self._people_set)

        def __len__(self):
            return len(self._people_set)

        def __contains__(self, person):
            try:
                return person in self._people_set
            except AttributeError:
                return False

        def __repr__(self):
            return self._people_set.__repr__()

    class ItemDict(collections.MutableMapping):
        def internal_item(self, key):
            try:
                return next(k for k in self.store if key == k)
            except StopIteration:
                return None

        def __init__(self, owner, *args, **kwargs):
            self.owner = owner
            self.store = dict()
            self.update(dict(*args, **kwargs))

        def __getitem__(self, key):
            ik = self.internal_item(key)
            return self.store[ik] if ik is not None else 0

        def __getattr__(self, name):
            try:
                item = eval(name)
                return self.internal_item(item)
            except:
                raise AttributeError(name + "is not the name of a defined Item")

        def __setitem__(self, key, value):
            if not isinstance(key, Item):
                raise TypeError("ItemDict only accepts keys of the type Item; got {}".format(key))

            if value < 0:
                raise ValueError("ItemDict only accepts positive values plus zero")

            elif value == 0:
                if self.__contains__(key):
                    self.__delitem__(key)
                return

            elif self.__contains__(key):
                ik = self.internal_item(key)
                self.store[ik] = value

            else:
                new_key = deepcopy(key)
                new_key.holder = self.owner
                self.store[new_key] = value

        def __delitem__(self, key):
            ik = self.internal_item(key)
            del self.store[ik]

        def __iter__(self):
            return iter(self.store)

        def __len__(self):
            return len(self.store)

        def __contains__(self, key):
            ik = self.internal_item(key)
            return ik in self.store

        def __repr__(self):
            return self.store.__repr__()

    class StatDict(collections.MutableMapping):
        def __init__(self, owner, *args, **kwargs):
            self.owner = owner
            self.store = {}
            self.store.update(dict(*args, **kwargs))

        def __getitem__(self, key):
            return self.store[key]

        def __setitem__(self, key, value):
            if not isinstance(key, basestring):
                raise TypeError("StatDict only accepts keys of the type basestring; got {}".format(key.__class__))

            if isinstance(value, int):
                value = ext_int(value)
            elif isinstance(value, float):
                value = ext_int(round(value))
            else:
                raise TypeError("StatDict only accepts values of the type int or float(converts them to int); got {}".format(key.__class__))

            delta_value = value - (self.store[key] if key in self.store else 0)
            short_name = 'player' if isinstance(self.owner, Player) else self.owner.short_name
            self.store[key] = value
            if delta_value > 0:
                if renpy.has_label(short_name+ "_" + key + '_positive_change'):
                    delayed_labels.append(short_name + "_" + key + '_positive_change')
            elif delta_value < 0:
                if renpy.has_label(short_name + "_" + key + '_negative_change'):
                    delayed_labels.append(short_name + "_" + key + '_negative_change')
            else:
                if renpy.has_label(short_name + "_" + key + '_no_change'):
                    delayed_labels.append(short_name + "_" + key + '_no_change')

        def __delitem__(self, key):
            del self.store[key]

        def __iter__(self):
            return iter(self.store)

        def __len__(self):
            return len(self.store)

        def __contains__(self, key):
            return key in self.store

        def __repr__(self):
            return self.store.__repr__()

    class LabelList(collections.MutableSequence):

        def check_value(self, label):
            if not isinstance(label, basestring):
                raise TypeError
            else:
                return True

        def __init__(self, owner, *args):
            self.owner = owner
            self.store = []
            self.store.extend([(l if not l.startswith("_") else owner.short_name + l) for l in list(args) if self.check_value(l)])

        def __getitem__(self, index):
            return self.store[index]

        def __setitem__(self, index, label):
            self.check_value(label)
            label = label if not label.startswith("_") else self.owner.short_name + label
            self.store[index] = label

        def __delitem__(self, index):
            del self.store[index]

        def __len__(self):
            return len(self.store)

        def insert(self, index, label):
            self.check_value(label)
            label = label if not label.startswith("_") else self.owner.short_name + label
            self.store.insert(index, label)

        def __repr__(self):
            return self.store.__repr__()

    class NotifyList(collections.MutableSequence):
        def __init__(self):
            self.store = []

        def __getitem__(self, index):
            return self.store[index][0] + (" x" + str(self.store[index][1]) if self.store[index][1] > 1 else "")

        def __setitem__(self, index, message):
            try:
                current_index = [m for m, q in self.store].index(message)
            except ValueError:
                self.store[index] = (message, 1)
                return

            self.store[current_index] = (message, self.store[current_index][1] + 1)

        def __delitem__(self, index):
            del self.store[index]

        def __len__(self):
            return len(self.store)

        def insert(self, index, message):
            try:
                current_index = [m for m, q in self.store].index(message)
            except ValueError:
                self.store.insert(index, (message, 1))
                return

            self.store[current_index] = (message, self.store[current_index][1] + 1)

        def __repr__(self):
            return self.store.__repr__()

    class LabelListWithPriority(collections.MutableSequence):

        def cmp_priority(self, a, b):
            if a == 'first' or b == 'last':
                return -1
            elif a == 'last' or b == 'first':
                return 1
            else:
                return cmp(a, b)

        def check_special_priorities(self, priority):
            if priority in ('first', 'last') and [l for l in self.store if l[1] == priority]:
                raise ValueError('There is already a priority ' + priority + ' assigment')

        def __init__(self, *args):
            self.store = []
            self.store.extend(list(args))
            self.auto_sort()

        def __getitem__(self, index):
            return self.store[index]

        def __setitem__(self, index, tuple):
            self.check_special_priorities(t[1])
            self.store[index] = tuple
            self.auto_sort()

        def __delitem__(self, index):
            del self.store[index]

        def __len__(self):
            return len(self.store)

        def insert(self, index, label, priority = 0):
            self.check_special_priorities(priority)
            self.store.insert(index, (label, priority))
            self.auto_sort()

        def auto_sort(self):
            self.store.sort(cmp = self.cmp_priority, key = lambda t: t[1])

        def __repr__(self):
            return self.store.__repr__()

        @property
        def label_list(self):
            return [l for l, p in self.store]

        def has(self, label):
          for l in self.label_list:
            if l == label:
              return True
          return False

        def append(self, label, priority = 0):
            self.check_special_priorities(priority)
            self.store.append((label, priority))
            self.auto_sort()

        def extend(self, label_list, priority = 0):
            for label in label_list:
                self.append(label, priority)

        def remove(self, label):
            for i in xrange(0, len(self.store)):
                if self.store[i][0] == label:
                    self.store.remove(self.store[i])
                    return
            raise ValueError ("Value not found for remove in LabelListWithPriority")



    ###
    # WT Classes
    ###

    ##
    # UI Classes
    ##

     # UI Space class to add more space to buttons
    class UISpace(renpy.store.object):
        def __init__(self, value, button_weight):
            self.value = value
            self.button_weight = button_weight
            self.unseen = False

     # Mod handling class
    class Package(renpy.store.object):
        def __init__(self, active, name, full_name, author, description, pregame_labels, dependencies, conflicts):
            self.active = active
            self.name = name
            self.author = author
            self.full_name = full_name
            self.description = description
            self.pregame_labels = pregame_labels
            self.dependencies = dependencies
            self.conflicts = conflicts

    # Package handling
    persist.packages = []
    persist.ordered_packages_by_dependencies = []

    # This class will handle keeping track of conditional costs for the actions
    class CostModifier(renpy.store.object):
        def __init__(self, flat, absolute, condition, name):
            self.name = name
            self.flat = flat
            self.absolute = absolute
            self.condition = condition

        def __repr__(self):
            return "<{}: F({}) A({}) C({})>".format(self.name, self.flat, self.absolute, self.eval_modifier)

        @property
        def eval_modifier(self):
            try:
                value = eval(self.condition.strip(), locals = locals()['self'].__dict__)
                if value in [True, False]:
                    return value
                else:
                    renpy.error("For cost modifier {}: condition did not eval to True or False.".format(self.name))
            except:
                renpy.error("For cost modifier {}: condition does not eval to correct syntax.".format(self.name))

    # Small class to handle variable individual values that exists outside actions
    class VariableNumber(renpy.store.object):
        def __init__(self, start_value, costs_modifiers = None):
            self.start_value = start_value
            self.costs_modifiers = [] if costs_modifiers is None else costs_modifiers

        @property
        def value(self):
            final_value = self.start_value
            if len(self.costs_modifiers) > 0:
                for modifier in self.costs_modifiers:
                    if modifier.eval_modifier:
                        if modifier.absolute is not None:
                            return modifier.absolute

                        final_value  += modifier.flat

            return final_value

        def add_modifier(self, flat = 0, absolute = None, condition = 'True', name = 'Unnamed'):
            modifier = CostModifier(flat, absolute, condition, name)
            self.costs_modifiers.append(modifier)
            return modifier

        def remove_modifier(self, modifier):
            if modifier in self.costs_modifiers:
                self.costs_modifiers.remove(modifier)

    # Class to handle choice that can de added to expandable menu
    class Choice(renpy.store.object):
        def __init__(self, name, to, condition, one_shot, **kwargs):
            self.variables = kwargs
            self.name = name
            self.to = to
            self.condition = condition
            self.one_shot = one_shot
            self.reopens_menu_once = False

        @property
        def eval_condition(self):
            try:
                value = eval(self.condition.strip(), locals = locals()['self'].__dict__)
                if value in [True, False]:
                    return value
                else:
                    renpy.error("For choice {}: condition did not eval to True or False.".format(self.name))
            except:
                renpy.error("For choice {}: condition does not eval to correct syntax.".format(self.name))

    # ExpandableMenu is a class to handle display renpy native menues that modder should be able to expand
    class ExpandableMenu(renpy.store.object):
        def __init__(self, title, parent = None, cancelable = True, cancel_text = None, chain_cancelable = False, chain_cancel_text = None, pre_label = None, post_label = None):
            self.title = title
            self.parent = parent
            self.cancelable = cancelable
            self.cancel_text = cancel_text
            self.chain_cancelable = chain_cancelable
            self.chain_cancel_text = chain_cancel_text
            self.pre_label = pre_label
            self.post_label = post_label
            self.choices = []
            self.reopens_once = False

        def add_choice(self, name, to, condition = "True", one_shot = False, **kwargs):
            choice = Choice(name, to, condition, one_shot, **kwargs)
            if choice not in self.choices:
                if isinstance(choice.to, ExpandableMenu):
                    choice.to.parent = self
                self.choices.append(choice)
                return choice
            return None

        def remove_choice(self, choice):
            if choice in self.choices:
                self.choices.remove(choice)
                return True
            return False

        def reopen_once(self):
            expandable_menu.reopens_once = True

    # Actions are the base of the modular system.
    # Actions allow for modders to add content wherever they want.
    # They can add new actions to an existing girl. They can add actions to a location, to an item, etc.
    # Actions should not be created directly, but using the add_action method in the Actionable class
    class Action(renpy.store.object):
        def __init__(self, _owner, name, label, new_context, context, costs, order, condition, is_button, auto_image, button_weight, allow_button_on_scene, use_owner_portrait, locked_menu, costs_modifiers, **eval_vars):
            self._owner = _owner
            self.name = name
            self.label = label
            self.seen_result = False if label or context.endswith('_connection') else True
            self.new_context = new_context
            self.context = context
            self.costs = costs
            self.costs_modifiers = dict() if costs_modifiers is None else costs_modifiers
            self.order = order
            self.condition = condition
            self.backed_condition = condition
            self.is_button = is_button
            self.auto_image = auto_image
            self.button_weight = button_weight
            self.allow_button_on_scene = allow_button_on_scene
            self.use_owner_portrait = use_owner_portrait
            self.locked_menu = locked_menu
            self.unseen = True
            self.ends_day_icon = False
            self.blocks_notify = False
            self.backtrack = False
            self.screen_hide_tag = None
            self.screen_show = None
            self.__dict__.update(**eval_vars)

        def __repr__(self):
            return "<{}[{}]): {}>".format(type(self).__name__, self._owner.name if self._owner else "", self.evaled_name)

        @property
        def owner(self):
            return self._owner

        # Return the actions within the owner that can generate this action's context
        # Returns [] if context is "_top_level"
        @property
        def parents(self):
            if not isinstance(self.owner, Actionable):
                raise ValueError("Owner not an Actionable")

            return [a for a in self.owner.actions if a.new_context == self.context]

        # Return the actions within the owner that share this action's context
        @property
        def siblings(self):
            if not isinstance(self.owner, Actionable):
                raise ValueError("Owner not an Actionable")

            return [a for a in self.owner.actions if a.context == self.context and a != self]

        # Return the actions within the owner that can have context of this action's new_context
        # Returns [] if we have no new_context
        @property
        def children(self):
            if not isinstance(self.owner, Actionable):
                raise ValueError("Owner not an Actionable")

            return [a for a in self.owner.actions if a.context == self.new_context]

        @property
        def is_valid_leaf(self):
            parents = self.parents
            if len(parents) > 0 and len([parent for parent in parents if parent.eval_action() and parent.is_valid_leaf]) == 0:
                return False

            return True

        @property
        def is_unseen(self):
            if self.is_valid_leaf:
                return self.eval_action() and (len([c for c in self.children if c.is_unseen]) > 0 or (self.unseen and self.label != ""))

            return False

        def make_seen(self):
            self.unseen = not self.seen_result if self.label or self.context.endswith('_connection') else False
            #renpy.restart_interaction()

        # Recognized cateories will be flat, percentage and absolute
        # Flat is well, a flat delta applied to the cost
        # Absolute changes the cost of the action to this, always and it supercedes flat values
        def add_modifier(self, resource = 'energy', flat = 0, absolute = None, condition = 'True', name = 'Unnamed'):
            modifier = CostModifier(flat, absolute, condition, name)
            self.costs_modifiers[resource].append(modifier)
            return modifier

        def remove_modifier(self, modifier, resource = 'energy'):
            if resource in self.costs_modifiers and modifier in self.costs_modifiers[resource]:
                self.costs_modifiers[resource].remove(modifier)

        def modified_cost(self, resource):
            # Check for int caveat
            if isinstance(self.costs, int):
                if resource != 'energy':
                    raise KeyError("Action {}: Resource {} is not in the costs".format(self.name, resource))
                    return

                final_value = self.costs
                if 'energy' in self.costs_modifiers:
                    for modifier in self.costs_modifiers['energy']:
                        if modifier.eval_modifier:
                            if modifier.absolute is not None:
                                return modifier.absolute

                            final_value  += modifier.flat

                return final_value

            else:
                if resource not in self.costs:
                    raise KeyError("Action {}: Resource {} is not in the costs".format(self.name, resource))
                    return

                final_value = self.costs[resource]
                if resource in self.costs_modifiers:
                    for modifier in self.costs_modifiers[resource]:
                        if modifier.eval_modifier:
                            if modifier.absolute is not None:
                                return modifier.absolute

                            final_value  += modifier.flat

                return final_value

        # Return true if the cost of the action is zero for every resource possible
        def is_zero_charge(self):

            if isinstance(self.costs, int):
                return self.modified_cost('energy') == 0

            elif isinstance(self.costs, dict):
                for key in self.costs:
                    if self.modified_cost(key) != 0:
                        return False
                return True

            else:
                raise TypeError("For action {}, costs is neither a dict nor an int".format(self.name))


        # Will deduct costs of the action from an actionable object (player, item, location, person)
        # Note that charge_costs will put you into negatives. A call to can_charge should be made if you want to gate costs
        def charge_costs(self, actionable):
            if isinstance(self.costs, int):
                try:
                    if self.modified_cost('energy') != 0:
                        actionable.delta_stat('energy', -self.modified_cost('energy'), with_notify = True)
                except KeyError:
                    raise KeyError("Action {}: Actionable {} has no energy stat".format(self.name, actionable.short_name))

            elif isinstance(self.costs, dict):
                try:
                    must_notify = False
                    for stat in self.costs:
                        if self.modified_cost(stat) != 0:
                            actionable.delta_stat(stat, -self.modified_cost(stat))
                            must_notify = True
                    if must_notify:
                        notify()
                except KeyError:
                    raise KeyError("Action {}: Actionable {} is missing a cost in its stats".format(self.name, self.cost))
            else:
                raise TypeError("For action {}, costs is neither a dict nor an int".format(self.name))

        # Return True if charging the action costs will not put any resource into negative numbers
        def can_charge(self, actionable):
            if isinstance(self.costs, int):
                try:
                    min_energy = actionable.stats['min_energy'] if 'min_energy' in actionable.stats else 0
                    return actionable.stats['energy'] - min_energy >= self.modified_cost('energy')
                except KeyError:
                    raise KeyError("Action {}: Actionable {} has no energy stat".format(self.name, actionable.short_name))

            elif isinstance(self.costs, dict):
                try:
                    for stat in self.costs:
                        minimum_value = actionable.stats['min_' + stat] if 'min_' + stat in actionable.stats else 0
                        if actionable.stats[stat] - minimum_value < self.modified_cost(stat):
                            return False
                    return True
                except KeyError:
                    raise KeyError("Action {}: Actionable {} is missing a cost in its stats".format(self.name, self.cost))
            else:
                raise TypeError("For action {}, costs is neither a dict nor an int".format(self.name))

        # Return a string that tell the costs to the UI. Uses a format like "Costs Y Energy, Costs Z money"
        @property
        def costs_to_words(self):
            if isinstance(self.costs, int):
                if self.modified_cost('energy') == 0:
                    return ""

                elif self.modified_cost('energy') > 0:
                    return "Costs {} {}".format(self.modified_cost('energy'), stats['energy'])

                else:
                    return "Gains {} {}".format(-self.modified_cost('energy'), stats['energy'])

            elif isinstance(self.costs, dict):
                try:
                    s = []
                    for stat in self.costs:
                        if self.modified_cost(stat) > 0:
                            s.append("Costs {} {}".format(self.modified_cost(stat), stats[stat]))
                        elif self.modified_cost(stat) < 0:
                            s.append("Gains {} {}".format(-self.modified_cost(stat), stats[stat]))
                except KeyError:
                    raise KeyError("For action {} a cost is not in the stat translation dict".format(self.stat))
                return ", ".join(s)

            else:
                raise TypeError("For action {}, costs is not a dict or an int".format(self.name))

        # Returns a string with what costs are missing for this action to be able to occur.
        # For now this is throwing its data directly to notify, but it should change once we have an UI
        def fail_costs_to_words(self, actionable, color = '#F00'):

            if isinstance(self.costs, int):
                try:
                    if actionable.stats['energy'] < self.modified_cost('energy'):
                        return "Not enough energy"
                except KeyError:
                    raise KeyError("Action {}: Actionable {} has no energy stat".format(self.name, actionable.short_name))

            elif isinstance(self.costs, dict):
                try:
                    for key in self.costs:
                        if actionable.stats[key] < self.modified_cost(key):
                            return "Not enough {}".format(stats[key])
                except KeyError:
                    raise KeyError("Action {}: Actionable {} is missing a cost in its stats".format(self.name, actionable.short_name))
            else:
                raise TypeError("For action {}, costs is neither a dict nor an int".format(self.name))

            return ""

        # Consolidates costs and gains into costs. You NEED to run this if you change an actions costs or gains
        def consolidate_costs(self):
            # Integrating costs and gains
            if isinstance(self.costs, int):
                self.costs = { 'energy' : self.costs }

            if isinstance(self.gains, int):
                self.gains = { 'energy' : self.gains }

            for key in self.costs.viewkeys() & self.gains.viewkeys():
                self.costs[key] -= self.gains[key]
                del self.gains[key]
            self.costs.update({k: -v for k, v in self.gains.items()})


        # Return True or False if the condition for the action evalues to True or False. Raises an error if it evalues to anything else
        def eval_action(self):
            try:
                value = eval(self.condition.strip(), locals = locals()['self'].__dict__)
                if value in [True, False]:
                    return value
                else:
                    renpy.error("For action {}: condition did not eval to True or False.".format(self.name))
            except:
                renpy.error("For action {} in {}: condition does not contain correct syntax.".format(self.name, self.owner.name))

        @property
        def evaled_name(self):
            return self.evaled_var('name')

        def evaled_var(self, var):
            try:
                if self.__dict__[var].startswith('^'):
                    return eval(self.__dict__[var][1:].strip(), locals = locals()['self'].__dict__)
                else:
                    return self.__dict__[var]
            except:
                renpy.error("For Action {}: stat {} does not have correct syntax".format(self.name, var))

    """
    WTText is a special kind of action that doesn't to anything but show non-interactive text in the UI in a different format.
    """
    class WTText(Action):
        def __init__(self, _owner, name, context, order, condition = 'True', **eval_vars):
            Action.__init__(self, _owner, name, "", "", context, 0, order, condition, False, '', 0, False, False, False, **eval_vars)
            self.unseen = False

    # Class to handle adding phrases to the examine top section
    class ExaminePhrase(renpy.store.object):
        def __init__ (self, condition, single_phrase, plurality = "False", plural_phrase = None):
            self.condition = condition
            self.single_phrase = single_phrase
            self.plurality = plurality
            self.plural_phrase = plural_phrase

        @property
        def phrase(self):
            if self.eval_plurality and self.plural_phrase is not None:
                return self.plural_phrase
            else:
                return self.single_phrase

        @property
        def eval_condition(self):
            try:
                value = eval(self.condition.strip(), locals = locals()['self'].__dict__)
                if value in [True, False]:
                    return value
                else:
                    renpy.error("For examine phrase {}: condition did not eval to True or False.".format(self.single_phrase))
            except:
                renpy.error("For examine phrase {}: condition does not eval to correct syntax.".format(self.single_phrase))

        @property
        def eval_plurality(self):
            try:
                value = eval(self.plurality.strip(), locals = locals()['self'].__dict__)
                if value in [True, False]:
                    return value
                else:
                    renpy.error("For examine phrase {}: plurality did not eval to True or False.".format(self.single_phrase))
            except:
                renpy.error("For examine phrase {}: plurality does not eval to correct syntax.".format(self.single_phrase))

    """
    Actionable is the class that _everything_ is based on
    Actionable allows objects that build on it to ask for lists of actions using context.
    Also to have stats, items and tags
    The default condition is "True" aka always present
    Short name is used as a prefix for labels and context if either of those start with "_"
    short_name NEEDS TO BE UNIQUE! Note that Actionable init fails for repeated short_names.
    If you call a variable that is not directly found on the object the class will then search stats for it.
    So client.desire is equivalent to client.stats['desire']
    """
    class Actionable(renpy.store.object):
        def __init__(self, short_name, cut_portrait = True):
            if short_name in all_short_names:
                raise ValueError("short_name '{}' already exists!".format(short_name))
            self.short_name = short_name
            self.has_portrait_image = renpy.has_image(short_name + "_portrait")
            self.portrait = short_name + "_portrait" if self.has_portrait_image else None
            self.cut_portrait = cut_portrait
            self.image = short_name + "_image"
            self.actions = []
            self.story_tags = set()
            self.tags = set()
            self.stats = StatDict(self)
            self.temporary_stat_modifiers = {}
            self.items = ItemDict(self)

            # UI
            self.buttons = []
            self.consolidating_changes = False
            self.consolidated_changes = {}
            self.examine_phrases = []

            # Store
            self.store_items = []
            self.discount_ratio = 1
            self.store_action = None

            all_short_names.append(self.short_name)
            all_actionables.append(self)

        def __getattr__(self, name):
            if 'stats' not in self.__dict__:
                raise AttributeError(name)
            elif name in self.__dict__['stats']:
                return self.stats[name]

            else:
                try:
                    item = eval(name)
                    return self.items[item]
                except:
                    raise AttributeError(name)

        def __setattr__(self, name, value):
            if 'stats' not in self.__dict__ or name not in self.__dict__['stats']:
                object.__setattr__(self, name, value)
            else:
                self.__dict__['stats'][name] = value

        ##
        # Shared
        ##

        # Returns true if the actionable has all the tags and items given
        def has(self, *args):
            for arg in args:
              if arg not in self.items and arg not in self.tags:
                  return False
            return True

        @property
        def is_unseen(self):
            return len([a for a in self.actions if a.eval_action() and a.is_unseen]) > 0

        def add_examine_phrase(self, condition, single_phrase, plurality = "False", plural_phrase = None):
            examine_phrase = ExaminePhrase(
                condition = condition,
                single_phrase = single_phrase,
                plurality = plurality,
                plural_phrase = plural_phrase
            )

            self.examine_phrases.append(examine_phrase)
            return examine_phrase

        def remove_examine_phrase(self, examine_phrase):
            if examine_phrase in self.examine_phrases:
                self.examine_phrases.remove(examine_phrase)
                return True

            return False

        ##
        # Actions Section
        ##

        # Get all the actions that evaled True for a particular context
        def get_evaled_actions(self, in_context = "_top_menu"):
            in_context = self.short_name + in_context if in_context.startswith("_") else in_context
            return [a for a in self.actions if a.eval_action() and a.context == in_context]

        def get_menu_objects(self, in_context):
            return self.get_evaled_actions(in_context)

        """
        Allows to create actions on the actionable class
        name is the name the UI will take to show the action
        label is the label that the action will call when selected on the UI
        new_context changes the current context. when the context changes the UI shows all the actions that have that context
        context is what the UI uses to know  what actions to show.
        label, new_context and context add short_name as prefix if they start with a '_' to differenciate them

        costs are the resources needed to activate this action. It can take an integer, in which case default to energy, or a dict of { stat : cost }
        gains are the same as cost but they sum instead of remove
        order is used to sort actions on the list. order = -1 allows the system to auto place the action in the 0 to 59 bracket
          60 to 69   is empty by default
          70 to 79   is for connections
          80 to 89   is empty by default
          90 to 99   is for actions that need to show last
          100        is for back actions
        condition is a simple python expression used to know if the action should be available. If you need to pass especific data to the condition you can do it after it.
          condition = "my_variable > 100", my_variable = chelsea.some_weird_stat or condition = "client.some_weird_stat > 100", client = chelsea
          Usually you won't need to do this unless the variable changes depending on the situation its called
          condition = "starting_location.is_empty" doesn't need to you give it starting_location as it static and already defined
        """
        def add_action(self, name, label = "", new_context = "", context = "_top_menu", costs = 0, gains = 0, order = -1, condition = "True", is_button = False, auto_image = 'gui/button/wip_%s.png', button_weight = 0, allow_button_on_scene = False, use_owner_portrait = False, locked_menu = False, costs_modifiers = None, **eval_vars):

          # Determining my order number if not given.
          # Ignoring all order numbers 90 so we don't built up in say a "Back" order = 100.
            order_number = 0
            if order == -1:
                if len([a.order for a in self.actions if a.order < 60]) > 0:
                    while order_number < 60:
                        if len([a for a in self.actions if a.order == order_number]) > 0:
                            order_number += 0.1
                        else:
                            break
            else:
                order_number = order

            action = Action(
                _owner = self,
                name = name,
                label = self.short_name + label if label.startswith("_") else label,
                new_context = self.short_name + new_context if new_context.startswith("_") else new_context,
                context = self.short_name + context if context.startswith("_") else context,
                costs = costs,
                gains = gains,
                order = order_number,
                condition = condition,
                is_button = is_button,
                auto_image = auto_image,
                button_weight = button_weight,
                allow_button_on_scene = allow_button_on_scene,
                use_owner_portrait = use_owner_portrait,
                locked_menu = locked_menu,
                costs_modifiers = costs_modifiers,
                **eval_vars)

            # Integrating costs and gains
            action.consolidate_costs()

            # If we are a button we organize that
            if action.is_button:
                self.buttons.append(action)
                self.buttons.sort(key=lambda a: a.button_weight)
            else:
                self.actions.append(action)
                self.actions.sort(key=lambda a: a.order)

            return action

        # Adds a set of actions back into the main action list.
        def add_action_set(self, action_set):
            self.actions = list(set(self.actions) | action_set)
            self.actions.sort(key=lambda a: a.order)

        # Adds an action targeted on a person present at the same location
        def add_targeted_action(self, name, title, verb, new_context = '', context = "_top_menu", costs = 0, gains = 0, order = -1, condition = "True", **eval_vars):
            condition += " and len(player.other_people_in_room) > 0"
            return self.add_action(name, 'action_on_person', new_context, context, costs, gains, order, condition, title = title, verb = verb, **eval_vars)

        def add_button(self, name, label = "", new_context = "", costs = 0, gains = 0, condition = "True", auto_image = 'gui/button/wip_%s.png', button_weight = 0,  allow_button_on_scene = False, use_owner_portrait = False, **eval_vars):
            return self.add_action(name, label, new_context, "_button", costs, gains, -10, condition, True, auto_image, button_weight, allow_button_on_scene, use_owner_portrait, **eval_vars)

        # Adds a non-interactive text banner on the action menu with a slightly different format on the UI
        def add_text(self, name, context = "_top_menu", order = -1):

            # Determining my order number if not given.
            # Ignoring all order numbers 90 so we don't built up in say a "Back" order = 100.
            order_number = 0
            if order == -1:
                if len([a.order for a in self.actions if a.order < 60]) > 0:
                    while order_number < 60:
                        if len([a for a in self.actions if a.order == order_number]) > 0:
                            order_number += 0.1
                        else:
                            break
            else:
              order_number = order

            action = WTText(
              _owner = self,
              name = name,
              context = self.short_name + context if context.startswith("_") else context,
              order = order_number)

            self.actions.append(action)
            self.actions.sort(key=lambda a: a.order)

            return action

        # Removes an action from the actions list
        def remove_action(self, action):
            if action in self.actions:
                if action.is_button:
                    self.buttons.remove(action)
                else:
                    self.actions.remove(action)

        # Removes a list of actions from the main action list. Returns a list of the actins that were removed.
        def remove_action_set(self, action_set):
            self.actions = list(set(self.actions) - action_set)
            self.actions.sort(key=lambda a: a.order)

        def has_action_of_context(self, context = "_top_menu", with_condition = True):
            context = self.short_name + context if context.startswith('_') else context
            for a in self.actions:
                if a.context == context and (a.eval_action() or not with_condition):
                    return True
            return False

        ##
        # UI section
        ##

        # Changes portrait. If given a strin it changes it to that string; if given a number it changes to short_name + "_portrait_" + number (i.e. elsa_portrait_3)
        # Also changes has_portrait_image to True if the new portrait is found and allows to change cut_portrait directly
        # Return True if the new portrait exists
        def change_portrait(self, new_portrait, cut_portrait = True):
            if isinstance(new_portrait, int):
                new_portrait = self.short_name + "_portrait_" + str(new_portrait)

            # We accept whatever we were given regardless of existance. But we change has_portrait_image after checking.
            self.portrait = new_portrait
            self.cut_portrait = cut_portrait
            self.has_portrait_image = renpy.has_image(new_portrait)

            return self.has_portrait_image

        # Changes main representative image (RAGS equivalent of portrait).
        # If given a string it changes it to that string; if given a number it changes to short_name + "_image_" + number (i.e. elsa_image_3)
        # Return True if the new image exists
        def change_image(self, new_image):
            if isinstance(new_image, int):
                new_image = self.short_name + "_image_" + str(new_image)

            # We accept whatever we were given regardless of existance.
            self.image = new_image
            return renpy.has_image(self.image)


        ##
        # Tags Section
        ##

        # Return true if the actionable has this tag
        # You can also use 'tag' in actionable.tags
        def has_tag(self, tag):
            return tag in self.tags

        # Return true if the actionable has all the tags given
        def has_tags(self, *tags):
            return  set(tags) <= self.tags

        # Return True if the actionable has any of the given tags
        def has_any_tag(self, *tags):
            return not set(tags).isdisjoint(self.tags)

        # Adds a tag to the actionable. Return true if the tag was added.
        def add_tag(self, tag, story_tag = False):
            if story_tag and tag not in self.story_tags:
                self.story_tags.add(tag)

                if renpy.has_label(self.short_name + "_update_media"):
                    delayed_labels.append(self.short_name + "_update_media")

                return True

            if tag not in self.tags:
                self.tags.add(tag)
                if renpy.has_label(self.short_name + "_update_media"):
                    delayed_labels.append(self.short_name + "_update_media")
                return True

            return False

        # Removes a tag from the actionable. Return true if the tag was removed
        def remove_tag(self, tag):
            if tag in self.story_tags:
                self.story_tags.remove(tag)
                if renpy.has_label(self.short_name + "_update_media"):
                    delayed_labels.append(self.short_name + "_update_media")
                return True

            if tag in self.tags:
                self.tags.remove(tag)
                if renpy.has_label(self.short_name + "_update_media"):
                    delayed_labels.append(self.short_name + "_update_media")
                return True

            return False

        # Adds several tags to the actionable.
        def add_tags(self, *tags):
            self.tags |= set(tags)

        # Remove several tags from the actionable
        def remove_tags(self, *tags):
            self.tags -= set(tags)

        # Adds the tag if not present, or removes the tag if present
        def toggle_tag(self, tag):
            if tag in self.tags:
                self.remove_tag(tag)
            else:
                self.add_tag(tag)

        # This methods return True if the tag is present and removes it. Also adds the tag if not present and return False.
        def has_and_toggle_tag(self, tag):
            if tag in self.tags:
                self.remove_tag(tag)
                return True
            else:
                self.add_tag(tag)
                return False

        # Cycles over the given tags in order. If the stop_tag is found then it return the current tag until the stop_tag is removed
        # It adds the first tag if no given tag is present on actionable. It does this even if the stop_tag is present.
        def cycle_tags(self, *tags, **kwargs):
            stop_tag = kwargs['stop_tag'] if 'stop_tag' in kwargs else None

            if len(tags) == 0:
                raise ValueError("cycle_tags needs at least one tag as argument")

            # Find first tag in tags
            index = -1
            for tag in set(tags) & self.tags:
                index = tags.index(tag)
            if index == -1:
                self.add_tag(tags[0])
                return tags[0]

            # Get next tag if we are not stopped
            if stop_tag is None or stop_tag not in self.tags:
                self.remove_tag(tags[index])

                if index + 1  < len(tags):
                    self.add_tag(tags[index + 1])
                    return tags[index + 1]
                else:
                    self.add_tag(tags[0])
                    return tags[0]

            else:
                return tags[index]

        ##
        # Stats Section
        ##

        # Return True if the actionable has the stat
        def has_stat(self, stat):
            if stat in self.stats:
                return True
            return False

        # Return True if the actionable has a min_<stat> stat present
        def has_min(self, stat):
            return self.has_stat('min_' + stat)

        # Return the number for min_<stat>, or None if the stat if not present
        def get_min(self, stat):
            if self.has_min(stat):
                return self.stats["min_" + stat]
            return None

        # Return True if the actionable has a max_<stat> stat present
        def has_max(self, stat):
            return self.has_stat('max_' + stat)

        # Return the number for max_<stat>, or None if the stat if not present
        def get_max(self, stat):
            if self.has_max(stat):
                return self.stats["max_" + stat]
            return None

        # Sets a new value for the stat within min_<stat> and max_<stat> if they are present.
        # Return a tuple of (X, Y). X is true if the stat was changed to value. Y is the new value of the stat.
        # Return None if the stat is not present
        def set_stat(self, stat, value = 0):
            if self.has_stat(stat):
                return_value = True
                if self.has_min(stat) and value < self.get_min(stat):
                    value = self.get_min(stat)
                    return_value = False

                elif self.has_max(stat) and value > self.get_max(stat):
                    value = self.get_max(stat)
                    return_value = False

                self.stats[stat] = value
                return (return_value, value)

            else:
                return None

        # Adds a new stat to the actionable with the value given
        # If min or max are not None a new stat is added called min_<stat> or max_<stat> as it correspond with the value given.
        # add_stat won't override an already created stat, min_<stat> or max_<stat> unless force is True
        # Return the stat final value is present or None if the stat is present and force is False
        def add_stat(self, stat, value = 0, min = None, max = None, force = False):
            if not self.has_stat(stat) or force:

                if min is not None and (not self.has_min(stat) or force):
                    self.stats['min_' + stat] = min if not isinstance(min, int) else ext_int(min)

                if max is not None and (not self.has_max(stat) or force):
                    self.stats['max_' + stat] = max if not isinstance(max, int) else ext_int(max)

                self.stats[stat] = 0
                return self.set_stat( stat, value )

            else:
                return None

        # Adds stat using a structure of (stat = 0, stat = 0, stat = 0). Note that this won't ever override existing stats.
        def add_stats(self, **kwargs):
            for stat, value in kwargs.items():
                self.add_stat(stat, value)

        # Adds stat using a simple structure of ('stat', 'stat', 'stat', value = 0, force = False). Note that this won't ever override existing stats.
        def add_stats_with_value(self, *stats, **kwargs):
            if 'value' not in kwargs:
                kwargs['value'] = 0

            if 'force' not in kwargs:
                kwargs['force'] = False

            for stat in stats:
                self.add_stat(stat, kwargs['value'], force = kwargs['force'])

        # Remove a stat from the stat list, including max and min.
        def remove_stat(self, stat):
            if self.has_stat(stat):

                if self.has_min(stat):
                    del self.stats['min_' + stat]

                if self.has_max(stat):
                    del self.stats['max_' + stat]

                del self.stats[stat]
                return True
            else:
                return False

        """
        Changes a stat using the delta_value given
        inverse_color shows the positive color when the value reduces if True. The same happens if the stat is in the reverse_stat list.
        with_message queues a message in the notify list if True
        with_notify immediatly notifies all messages in the notify list if True
        Internally checks the for the presence of the show_[stat] tag and shows the stat if needed
        Return a tuple of (X, Y). X is True if the value actually changed. Y is the final value of stat.
        Return None if the stat is not present
        """
        def delta_stat(self, stat, delta_value, show_numbers = False, inverse_color = False, with_message = True, with_notify = False, reason = None, call_update_label = True):
            if self.has_stat(stat):
                backed_stat = self.stats[stat]
                self.set_stat(stat, backed_stat + delta_value)
                if with_message:

                    if self.consolidating_changes:
                        if stat in self.consolidated_changes:
                            self.consolidated_changes[stat] += self.stats[stat] - backed_stat
                        else:
                            self.consolidated_changes[stat] = self.stats[stat] - backed_stat
                    else:
                        if delta_value < 0 if inverse_color or stat in inverse_stats else delta_value > 0:
                            color = '#090' # Green #trying darker green
                            #color = '#0F0' # Green #original lime green
                        else:
                            color = '#F00' # Red

                        show_numbers = show_numbers or (player.has_tag("show_" + stat))

                        if backed_stat < self.stats[stat]:
                            if isinstance(self, Player):
                                notify_messages.append("Your {color=" + color + "}" + stats[stat] + "{/color} has been raised" + ((" by {color=" + color + "}" + str(delta_value) + "{/color}") if show_numbers else "") + ( " ({})".format(reason) if reason is not None else ""))

                            elif isinstance(self, (Person, Location, Item)):
                                notify_messages.append(self.name + "'s {color=" + color + "}" + stats[stat] + "{/color} has been raised" + ((" by {color=" + color + "}" + str(delta_value) + "{/color}") if show_numbers else "") + ( " ({})".format(reason) if reason is not None else ""))

                        elif backed_stat > self.stats[stat]:
                            if isinstance(self, Player):
                                notify_messages.append("Your {color=" + color + "}" + stats[stat] + "{/color} has been decreased" + ((" by {color=" + color + "}" + str(-delta_value) + "{/color}") if show_numbers else "") + ( " ({})".format(reason) if reason is not None else ""))

                            elif isinstance(self, (Person, Location, Item)):
                                notify_messages.append(self.name + "'s {color=" + color + "}" + stats[stat] + "{/color} has been decreased" + ((" by {color=" + color + "}" + str(-delta_value) + "{/color}") if show_numbers else "") + ( " ({})".format(reason) if reason is not None else ""))

                        else:
                            if isinstance(self, Player):
                                notify_messages.append("Your {color=#00F}" + stats[stat] + "{/color} did not change")

                            elif isinstance(self, (Person, Location, Item)):
                                notify_messages.append(self.name + "'s {color=#00F}" + stats[stat] + "{/color} did not change")

                        if with_notify:
                            notify()

                if call_update_label and renpy.has_label(self.short_name + "_update_media"):
                    delayed_labels.append(self.short_name + "_update_media")

        def create_delta_stat_message(self, stat, true_delta_value):
            if true_delta_value < 0 if stat in inverse_stats else true_delta_value > 0:
                color = '#090' # Green #trying darker green
                #color = '#0F0' # Green #original lime green
            else:
                color = '#F00' # Red

            show_numbers = player.has_tag("show_" + stat)

            if true_delta_value > 0:
                if isinstance(self, Player):
                    notify_messages.append("Your {color=" + color + "}" + stats[stat] + "{/color} has been raised" + ((" by {color=" + color + "}" + str(true_delta_value) + "{/color}") if show_numbers else ""))

                elif isinstance(self, (Person, Location, Item)):
                    notify_messages.append(self.name + "'s {color=" + color + "}" + stats[stat] + "{/color} has been raised" + ((" by {color=" + color + "}" + str(true_delta_value) + "{/color}") if show_numbers else ""))

            elif true_delta_value < 0:
                if isinstance(self, Player):
                    notify_messages.append("Your {color=" + color + "}" + stats[stat] + "{/color} has been decreased" + ((" by {color=" + color + "}" + str(-true_delta_value) + "{/color}") if show_numbers else ""))

                elif isinstance(self, (Person, Location, Item)):
                    notify_messages.append(self.name + "'s {color=" + color + "}" + stats[stat] + "{/color} has been decreased" + ((" by {color=" + color + "}" + str(-true_delta_value) + "{/color}") if show_numbers else ""))

            else:
                if isinstance(self, Player):
                    notify_messages.append("Your {color=#00F}" + stats[stat] + "{/color} did not change")

                elif isinstance(self, (Person, Location, Item)):
                    notify_messages.append(self.name + "'s {color=#00F}" + stats[stat] + "{/color} did not change")


        def consolidated_change_messages(self):
            if len(self.consolidated_changes) > 0:
                for stat in self.consolidated_changes:
                    self.create_delta_stat_message(stat, self.consolidated_changes[stat])
                self.consolidated_changes = {}

        # Adds step to stat every time is called. Check delta_stat for comments on inverse_color, with_message and with_notify
        # Return a tuple (X, Y). X is True if the stat is over or equal to target (over is assumed depending on if step is positive or negative).
        # Y is the final value of stat (Mind that this is still bounded by min and max if present)
        # Return None if stat is not present
        def step_stat(self, stat, step, target = None, inverse_color = False, with_message = False, with_notify = False):
            if self.has_stat(stat):

                self.delta_stat(stat, step, inverse_color = False, with_message = with_message, with_notify = with_notify)

                if target is not None:
                    if step > 0:
                        return (self.stats[stat] >= target, self.stats[stat])
                    elif step < 0:
                        return (self.stats[stat] <= target, self.stats[stat])
                    else:
                        return (self.stats[stat] == target, self.stats[stat])
                return (None, self.stats[stat])

            return None

        # Returns the stat modified by owned items
        # If use_own_items is True owned items are used. If apply_inverse_to_items is True items substract from the stat instead of adding _if the stat is in the inverse_stats list_
        def moded_stat(self, stat, use_own_items = True, apply_inverse_to_items = False, with_temp_checks = True):
            own_items_mod = sum([i.stats[stat] for i in self.get_items() if i.has_stat(stat)]) if use_own_items else 0
            return_value =  (self.stats[stat] if self.has_stat(stat) else 0)  + (-own_items_mod if apply_inverse_to_items and stat in inverse_stats else own_items_mod)

            #Resolve temporary modifiers
            if with_temp_checks:
                self.resolve_temp_mod('check', stat)

            return return_value

        # Temporary modifiers
        def open_temp_group(self, group_name, duration = 1, duration_unit = 'day'):
            if duration_unit not in ['check', 'day']:
                raise ValueError("temp modifier duration unit not recognised: {}".format(duration_unit))

            self.current_temp_group_name = group_name
            self.temporary_stat_modifiers[group_name] = [duration_unit, duration]

        def close_temp_group(self, resolve_label = None, with_notify = True):
            self.temporary_stat_modifiers[self.current_temp_group_name].append(resolve_label)
            self.current_temp_group_name = None

            if with_notify:
                notify()

        def add_temp_mod(self, stat, value, show_numbers = False, with_message = True, with_notify_add = False, with_notify_resolve = False):
            if self.current_temp_group_name is None:
                print ("No open group for temporary modifiers")
                return

            self.delta_stat(stat, value, show_numbers, False, with_message, with_notify_add, self.current_temp_group_name)
            self.temporary_stat_modifiers[self.current_temp_group_name].append([stat, -value, show_numbers, False, with_message, with_notify_resolve, self.current_temp_group_name])

        def resolve_temp_mod(self, duration_unit = 'day', stat = None):
            #self.close_temp_group()
            for k, v in self.temporary_stat_modifiers.items():
                if v[0] == duration_unit:
                    if duration_unit == 'day':
                        v[1] -= 1
                    elif duration_unit == 'check':
                        renpy.store.v = v
                        if stat in [mod_list[0] for mod_list in v[2:-1]]:
                            v[1] -= 1

            for k, v in self.temporary_stat_modifiers.items():
                if v[0] == duration_unit and v[1] <= 0:
                    for temp_mod in v[2:-1]:
                        self.delta_stat(*temp_mod)
                    if v[-1] and renpy.has_label(v[-1] + "_removed"):
                        delayed_labels.append(v[-1] + "_removed")
                    del self.temporary_stat_modifiers[k]

        def added_by_items(self, stat):
            return sum([i.stats[stat] for i in self.get_items() if i.has_stat(stat)])

        ##
        # Items section
        ##

        # Return True if the actionable has a copy of the given item
        def has_item(self, item):
            return item in self.items

        def has_item_of_family(self, item):
            return item.family in [i.family for i in self.items]

        # Return the amount of items the actionable has
        def quantity(self, item):
            return self.items[item]

        """
        Adds the given quantity of item to the actionable.
        partial allows for less items to be added if the max_quantity of the item is less than the final quantity in inventory
        with_message and with_notify comments can be found in delta_stat
        Return a copy of the item instance in the inventory if items were added (Or the shared intance if the item is unitary).
        Returns False if no items were added.
        """
        def add_item(self, item, quantity = 1, partial = False, with_message = True, with_notify = False):

            # Max quantity of items possible taking sharing into account
            max_quantity = item.family.max_quantity if item.family.share_max_quantity else item.max_quantity

            # Is the item already on the inventory
            item_present = item in self.items

            # Amount of items in inventory taking sharing into account
            if item_present:
                current_quantity = sum([self.items[i] for i in self.items if i.is_family_of(item)]) if item.family.share_max_quantity else self.items[item]
            else:
                current_quantity = sum([self.items[i] for i in self.items if i.is_family_of(item)]) if item.family.share_max_quantity else 0

            # Final number of possible items taking sharing into account
            available_quantity = max_quantity - current_quantity

            if partial:
                quantity = max(1, min(quantity, available_quantity))
            else:
                quantity = max(1, quantity)

            if not item_present:
                if quantity <= available_quantity:
                    self.items[item] = 0
                else:
                    return None

            if quantity <= available_quantity:
                self.items[item] += quantity
                ii = self.items.internal_item(item)

                if isinstance(self, Player):
                    ii.in_inventory = True
                else:
                    ii.in_inventory = False

                if with_message:
                    if isinstance(self, Player):
                        notify_messages.append(str(quantity) + " " + item.name + " has been added to your inventory.")

                    elif isinstance(self, Person):
                        notify_messages.append(str(quantity) + " " + item.name + " has been added to " + self.name + "'s inventory.")

                    elif isinstance(self, Location):
                        notify_messages.append(str(quantity) + " " + item.name + " has been added to " + self.name)
                if with_notify:
                    notify()
                if item.unique:
                    item_key = None
                    for key, value in store.__dict__.iteritems():
                        if value == item:
                            item_key = key
                            break
                    store.__dict__[item_key] = ii

                if renpy.has_label(self.short_name + "_update_media"):
                    delayed_labels.append(self.short_name + "_update_media")

                return ii
            else:
                return None

        """
        Remove the given quantity of item to the actionable.
        partial allows for less items to be removed if there is not enough items to remove
        with_message and with_notify comments can be found in delta_stat
        Returns True if item was removed.
        Returns False if no items were removed.
        """
        def remove_item(self, item, quantity = 1, partial = False, with_message = True, with_notify = False):
            if item in self.items:

                if partial:
                    quantity = max(1, min(quantity, self.quantity(item)))
                else:
                    quantity = max(1, quantity)

                if self.items[item] >= quantity:
                    self.items[item] -= quantity

                    if with_message:
                        if isinstance(self, Player):
                            notify_messages.append(str(quantity) + " " + item.name + " has been removed from your inventory.")

                        elif isinstance(self, Person):
                            notify_messages.append(str(quantity) + " " + item.name + " has been removed from " + self.name + "'s inventory.")

                        elif isinstance(self, Location):
                            notify_messages.append(str(quantity) + " " + item.name + " has been removed from " + self.name)

                    if with_notify:
                        notify()

                    if renpy.has_label(self.short_name + "_update_media"):
                        delayed_labels.append(self.short_name + "_update_media")

                    return True
                else:
                    return False
            else:
                return False

        # Return a list of all the copies of the items in the inventory without quantities
        def get_items(self, family = None, show_hidden = False):
            return [i for i in self.items if (not i.hidden or show_hidden) and (i.family == family.family if family is not None else True)]

        # Return true if the actionable has enough items to give
        def can_give(self, item, quantity = 1):
            return self.quantity(item) >= quantity

        # Returns True if the actionable has enough space to recieve the quantity of items
        def can_receive(self, item, quantity = 1):
            if item.family.share_max_quantity:
                return sum([self.quantity(i) for i in self.items if i.is_family_of(item)]) + quantity <= item.family.max_quantity
            else:
                return self.quantity(item) + quantity <= item.max_quantity

        # Return True if both can_give and can_receive test True
        def can_deliver(self, item, receiver, quantity = 1):
            return self.can_give(item, quantity) and receiver.can_receive(item, quantity)

        """
        Gives quantity of item from actionable to reciever
        Checks if can_deliver is True before moving the Items
        partial tries to adjust the quantity of items based on amount in inventory and space in the reciever if True
        with_message and with_notify comments are in delta_stat
        Returns the instance of the item if added, or False if no items were moved
        """
        def give_item(self, item, receiver, quantity = 1, partial = False, with_message = True, with_notify = False, always_remove = False):
            if partial:
                quantity = min(1, quantity, self.quantity(item), item.max_quantity - person.quantity(item))
            else:
                quantity = max(1, quantity)

            if self.can_deliver(item, receiver, quantity):
                if receiver.items[item] == 0:
                    # Need to mark current action as seen earlier here so the object copy carries that change
                    # if action is not None:
                    #     action.unseen = False
                    internal_item = self.items.internal_item(item)
                    self.remove_item(item, quantity, with_message)
                    return receiver.add_item(internal_item, quantity, with_message, with_notify = with_notify)
                else:
                    self.remove_item(item, quantity, with_message)
                    return receiver.add_item(item, quantity, with_message, with_notify = with_notify)

            elif always_remove and self.can_give(item, quantity):
                self.remove_item(item, quantity, with_message, with_notify = with_notify)
                return receiver.items.internal_item(item)

            return False

        """
        Adds an item to the store of this actionable
        If available_quantity is over 50 no amount is shown as the item is concidered endless
        If send_to is not None, it should be a location to were the item is send when bought.
        discount_ratio is a multiplier thjat applies to all items in the store
        Returns the ItemInStore instance if added. Or None if no item was added.
        """
        def get_store_item(self, item):
            for store_item in self.store_items:
                if store_item.item == item:
                    return store_item
            return None

        def add_store_item(self, item, available_quantity = -1, price = 0, send_to = None, discount_ratio = 1, single_buy_amount = 1, with_examine = False, seen = False):
            for item_in_store in [i for i in self.store_items if i.item == item]:
                self.store_items.remove(item_in_store)

            item_in_store = ItemInStore(self, item, available_quantity, price, send_to, discount_ratio, single_buy_amount, with_examine, seen)
            self.store_items.append(item_in_store)
            self.sort_store()
            return item_in_store

        # Adds the store action to the top menu actions
        def open_store(self, store_name = "Buy", button_weight = 0, force = False):
            if force or self.store_action is None:
                self.store_action = self.add_button(store_name, new_context = 'store', auto_image = 'gui/button/shopping_cart_%s.png', button_weight = button_weight)
            else:
                self.buttons.append(self.store_action)
                self.buttons.sort(key=lambda a: a.button_weight)

        # Removes the store action from the list
        def close_store(self):
            self.remove_action(self.store_action)

        # Sorts the items in the store by price
        def sort_store(self):
            self.store_items.sort(key = lambda item: item.price)

        # Adds an action to all the items in the store. As long as the store is open
        def add_action_to_store_items(self, name, label = "", new_context = "", context = "_top_menu", costs = 0, gains = 0, order = -1, condition = "True", **eval_vars):
            for item in self.store_items:
                item.add_action(name, label = label, new_context = new_context, context = context, costs = costs, gains = gains, oreder = order, condition = condition, **eval_vars)

    ####
    # Items section
    ####

    """
    Item base class
    Note that a single instance is shared between all items in inventories. Any change on the key item of an inventory will reflect on all other inventory instance
    hidden makes an item not apprear when the get_items method is called. Good for hidden modifiers like the bonsai aura when fully grown.
    with_examine adds an examine action that calls the label short_name + "_examine"
    You can add any stats that you want at the end. The item won't overwrite if you add for example desire_mod
    """

    class Item(Actionable):
        def __init__(self, name, short_name, cut_portrait = True, max_quantity = 1, hidden = False, with_examine = False, with_give = False, with_use = False, family = None, share_max_quantity = True, unique = False,  **stats):
            Actionable.__init__(self, short_name, cut_portrait)
            self.unique = unique
            self.name = name
            self.family = self if family is None else family
            self.share_max_quantity = share_max_quantity if family is None else False
            self.hidden = hidden
            self.max_quantity = max_quantity
            self.in_inventory = False
            self.examine_action = self.add_action("^'Examine ' + _owner.name", label = "_examine", condition = "'examinable' in item.tags", item = self, unseen = False, seen_result = True)
            self.give_action = self.add_targeted_action("^ 'Give ' + _owner.name", title = "^ 'Give ' + _owner.name + ' to whom?'", verb = 'give', condition = "'givable' in _owner.tags and _owner.in_inventory", item = self)
            self.use_action = self.add_targeted_action("^ 'Use ' + _owner.name", title = "^ 'Use ' + _owner.name + ' on whom?'", verb = 'use', condition = "'usable' in _owner.tags  and _owner.in_inventory", item = self)

             # Adding Stats that may be missing
            self.add_stats(**stats)
            self.add_stats_with_value('sos_mod', 'desire_mod', 'submission_mod', 'resistance_mod', 'hypnosis_level_mod', 'sos', 'desire', 'submission', 'resistance', 'hypnosis_level')

            if with_examine:
                self.add_tag('examinable')

            if with_give:
                self.add_tag('givable')

            if with_use:
                self.add_tag('usable')

            all_items.append(self)

        def __eq__(self, other):
            if other and isinstance(other, Item):
                return self.short_name == other.short_name
            return False

        def __ne__(self, other):
            return not self.__eq__(other)

        def __repr__(self):
            return "<{}[{}]: {}>".format(type(self).__name__, self.short_name, self.name)

        def is_family_of(self, item):
            return self.family == item.family

        def add_to(self, *args):
            for arg in args:
                if isinstance(arg, Actionable):
                    arg.add_item(self)

        def get_menu_objects(self, in_context):
            return self.get_evaled_actions(in_context)

    class ItemInStore(Actionable):
        def __init__(self, store, item, available_quantity, price, send_to, discount_ratio, single_buy_amount = 1, with_examine = False, seen = True):
            Actionable.__init__(self, item.short_name + '_' + store.short_name, False)
            self.store = store
            self.item = item
            self.available_quantity = available_quantity
            self.price = price
            self.send_to = send_to
            self.discount_ratio = discount_ratio
            self.single_buy_amount = min(single_buy_amount, item.max_quantity)

            if seen:
                self.buy_action = self.add_action("Buy", label = 'buy', conditions = "'buyable' in item.tags", item = self, unseen = False, seen_result = True)
                self.examine_action = self.add_action("Examine", label = "_examine", condition = "'examinable' in item.tags", item = self, unseen = False, seen_result = True)
            else:
                self.buy_action = self.add_action("Buy", label = 'buy', conditions = "'buyable' in item.tags", item = self)
                self.examine_action = self.add_action("Examine", label = "_examine", condition = "'examinable' in item.tags", item = self)

            self.add_tag('buyable')

            if with_examine:
                self.add_tag('examinable')

        # Return True if the item can be given to the reciever from the store (either player or place)
        def can_add_store_item(self):
            receiver = player if self.send_to is None else self.send_to
            return receiver.can_receive(self.item, self.single_buy_amount)

        def final_price(self):
            return int(round(self.price * min(self.discount_ratio, self.store.discount_ratio)))

        def get_menu_objects(self, in_context):
            return self.get_evaled_actions(in_context)

    ####
    # Locations section
    ####

    class Connection(Action):
        def __init__(self, _owner, location, name, context, costs, order, condition, costs_modifiers, **eval_vars):
            Action.__init__(self, _owner, name, "", "", context, costs, order, condition, False, "", 0, False, False, False, costs_modifiers, **eval_vars)
            self.location = location

        @property
        def is_unseen(self):
            return self.eval_action() and self.location.unseen

    class Location(Actionable):
        def __init__(self, name, short_name, cut_portrait = True, enter_break_labels = [], exit_break_labels = [], enter_labels = [], exit_labels = [], area = None, unseen = True, **stats):
            Actionable.__init__(self, short_name, cut_portrait)
            self.name = name
            self.enter_break_labels = LabelList(self, *enter_break_labels)
            self.enter_labels = LabelList(self, *enter_labels)
            self.exit_break_labels = LabelList(self, *exit_break_labels)
            self.exit_labels = LabelList(self, *exit_labels)
            self.area = [] if area is None else area
            self.people = PeopleSet(self)
            self.unseen = unseen

            # Adding Stats that may be missing
            self.add_stats(**stats)
            self.add_stats_with_value('sos_mod', 'desire_mod', 'submission_mod', 'resistance_mod', 'hypnosis_level_mod')

            self.add_button("", new_context = '_top_menu', use_owner_portrait = True, button_weight = 950)
            self.examine_action = self.add_action("Examine", label = "_examine", unseen = False, seen_result = True)
            self.navigation_action = self.add_button("Navigation", new_context = '_connection', condition="persistent.movement == 'button'", auto_image = "gui/button/navigation_%s.png", button_weight = 1000)

            all_locations.append(self)

        def __repr__(self):
            return "<{}[{}]: {}>".format(type(self).__name__, self.short_name, self.name)

        # Return all location including this one that share area
        @property
        def locations_in_area(self):
            if not self.area:
                return [self]
            elif isinstance(self.area, list) and len(self.area) == 1:
                return [l for l in all_locations if (self.area[0] == l.area if isinstance(l.area, list) else self.area[0] in l.area)]
            elif isinstance(self.area, basestring):
                return [l for l in all_locations if (self.area in l.area if isinstance(l.area, list) else self.area == l.area)]
            else:
                raise TypeError("locations_in_area variables are not basestring or lists")

        # Return True if the current location is this location
        @property
        def is_here(self):
            return current_location == self

        # Return True if this location is empty (ignores player unless count_player is True)
        @property
        def is_empty(self, count_player = False):
            return len([p for p in self.people if count_player or not isinstance(p, Player)]) == 0

        # Return the number of people in a location (ignores player unless count_player is True)
        @property
        def number_of_people(self, count_player = False):
            return len([p for p in self.people if count_player or not isinstance(p, Player)])

        """
        Adds special action Connection that serves to move between locations
        locations is the destination
        name is what the UI shows. If left as "" it'll default to the location's name
        costs, gains and condition are commented in add_action
        It tries to add the action to the 70-79 space
        Returns the added connection
        """
        def add_connection(self, location, name = None, costs = 0, gains = 0, order = -1, condition = "True", costs_modifiers = dict(), **eval_vars):

            # Determining my order number if not given.
            # Ignoring all order numbers 90 so we don't built up in say a "Back" order = 100.
            order_number = 70
            if order == -1:
                if len([a.order for a in self.actions if a.order >= 70 and a.order < 80]) > 0:
                    while order_number < 80:
                        if len([a for a in self.actions if a.order == order_number]) > 0:
                            order_number += 0.1
                        else:
                            break
            else:
                order_number = order

            connection = Connection(location =  location,
              _owner = self,
              name = name if name else location.name,
              context = self.short_name + "_connection",
              costs = costs,
              gains = gains,
              order = order_number,
              condition = condition,
              costs_modifiers = costs_modifiers,
              **eval_vars)

            # Integrating costs and gains
            connection.consolidate_costs()

            self.actions.append(connection)
            self.actions.sort(key=lambda a: a.order)

            return connection

        # Adds connection with the format (location, { stat: value, stat: value }, location, location, location, { stat: value, stat: value })
        # If no costs are given costs default to 0
        def add_connections(self, *connections):
            raw_data = list(connections)

            for i in xrange(0, len(raw_data)):
                if not isinstance(raw_data[i], Location):
                    continue

                location = raw_data[i]
                if i + 1 < len(raw_data) and isinstance(raw_data[i+1], (int, dict)):
                    costs = raw_data[i + 1]
                else:
                    costs = 0

                self.add_connection(location, costs = costs)

        def get_menu_objects(self, in_context):
            return self.get_evaled_actions(in_context)

        # Displays a menu of the people in the room ignoring the player
        def display_people_menu(self):
            people = PeopleSet(self, self.people)
            people.discard(player)

            if len(people) == 0:
                return None
            elif len(people) == 1:
                return tuple(people)[0]
            else:
                return renpy.display_menu(items=[(p.name, p) for p in people], interact=True, screen='choice')

        # Brings a person to the current location. If follows is True the follows tag is added.
        # While the follow tag is present the person will folow any movement we do using the move_to label
        def bring_person_here(self, person, follows = True):
            self.people.add(person)

            if follows:
                person.add_tag('follows')
            else:
                person.remove_tag('follows')

            if renpy.has_label(self.short_name + "_update_media"):
                delayed_labels.append(self.short_name + "_update_media")

    ####
    # People Section
    ####

    # Person is the base for classes that can talk
    class Talkative(Actionable):
        def __init__(self, character, short_name, cut_portrait = True, enter_break_labels = [], exit_break_labels = [], enter_labels = [], exit_labels = [], **stats):
            Actionable.__init__(self, short_name, cut_portrait)
            self.c = character
            self._location = None
            self.enter_break_labels = LabelList(self, *enter_break_labels)
            self.enter_labels = LabelList(self, *enter_labels)
            self.exit_break_labels = LabelList(self, *exit_break_labels)
            self.exit_labels = LabelList(self, *exit_labels)
            self.add_stats(**stats)

            # Tags
            self.remove_tags_daily = set()
            self.remove_tags_weekly = set()

        def __repr__(self):
            return "<{}[{}]: {}>".format(type(self).__name__, self.short_name, self.name)

        @property
        def name(self):
            return self.c.name

        @name.setter
        def name(self, value):
            self.c.name = value

        @property
        def location(self):
            return self._location

        @location.setter
        def location(self, location):
            location.people.add(self)

        def in_area(self, area):
            if self.location is not None:
                return self.location in locations_in_area(area)
            return False

        # Return true if this person location is None
        @property
        def is_nowhere(self):
            return location is None

        # Return all the other people in the room
        @property
        def other_people_in_room(self):
            return set(p for p in self.location.people if p != self) if self.location is not None else set()

        """
        Tests a stat against a value.
        use_own_items uses inventory items modifiers if True. Items in inventory sum to the stat if the _same_ stat is present.
        use_location sums location modifier if the <stat>_mod is present. use_location_items uses the location items if the <stat>_mod if present
        use_present_people sums people modifiers if the <stat>_mod is present. use_people_items sums people items if the <stat>_mod if present
        If stat is in inverse_stats test is concidered pased when stat is equal or under value. Else it needs to be over or equal to value.
        """
        def test(self, stat, test_value, stat_mod = 0, use_location = True, use_location_items = True, use_present_people = True, use_people_items = True, use_own_items = True, with_temp_checks = True):
            if stat.endswith(('_mod', '_gain')) :
                renpy.error("Talkative {} is trying to test a modifier {}. Did you mean to test {}?".format(self.name, stat, stat[:stat.find('_') - len(stat)]))

            if isinstance(test_value, basestring):
                if test_value.endswith(('_mod', '_gain')) :
                    renpy.error("Talkative {} is trying to test a modifier {}. Did you mean to test {}?".format(self.name, test_value, test_value[:test_value.find('_') - len(test_value)]))
                else:
                    final_test_value = self.modified_stat(test_value, use_location, use_location_items, use_present_people, use_people_items, use_own_items, with_temp_checks)
            else:
                final_test_value = test_value

            final_stat = self.modified_stat(stat, use_location, use_location_items, use_present_people, use_people_items, use_own_items, with_temp_checks) + stat_mod

            # Returning test result
            return final_stat < final_test_value if stat in inverse_stats else final_stat > final_test_value

        def modified_stat(self, stat, use_location = True, use_location_items = True, use_present_people = True, use_people_items = True, use_own_items = True, with_temp_checks = True):

            # Our stat and whatever our items are giving us
            current_stat = self.moded_stat(stat, use_own_items = use_own_items, with_temp_checks = with_temp_checks)

            # Location stat_mod and whatver its items are giving it
            if self.location is not None:
                location_stat_mod = self.location.moded_stat(stat + "_mod", use_own_items = use_location_items, with_temp_checks = with_temp_checks) if use_location and self.location is not None and self.location.has_stat(stat + "_mod") else 0

                # People present and whatever their items give them
                people_stat_mod = sum(p.moded_stat(stat + '_mod', use_own_items = use_people_items, with_temp_checks = with_temp_checks) for p in self.other_people_in_room) if use_present_people else 0
            else:
                location_stat_mod = 0
                people_stat_mod = 0

            # Returning modified stat value
            return current_stat + location_stat_mod + people_stat_mod

        """
        Changes a stat using a delta_value.
        Uses all possible modifiers.
        Own items need to have the _same_ stat. I.e. A client with desire_gain will get more desire when she gets it. And a client with an item with desire_gain will too
        Location or people need to have desire_gain_mod. So do items in Location or People.
        """
        def change_stat(self, stat, delta_value, show_numbers = False, with_message = True, with_notify = False, reason = None, with_temp_checks = True):
            # Check if we need to record this change
            if stat in recorded_stats and 'player' in renpy.store.__dict__ and ((delta_value > 0 and stat not in inverse_stats) or (delta_value < 0 and stat in inverse_stats)):
                player.add_stat(recorded_stats[stat]+"_action_count")
                player.stats[recorded_stats[stat]+'_action_count'] += 1

            # Check if we need to calculate stuff
            inverse = stat in inverse_stats
            if (delta_value > 0 and not inverse) or (delta_value < 0 and inverse):

                # Our stat and whatever our items are giving us
                self_stat_gain_mod = self.moded_stat(stat + "_gain", with_temp_checks = with_temp_checks)

                # Location stat_gain_mod and whatver its items are giving it
                location_stat_gain_mod = self.location.moded_stat(stat + "_gain_mod", with_temp_checks = with_temp_checks) if self.location is not None and self.location.has_stat(stat + "_gain_mod") else 0

                # People present and whatever their items give them
                people_stat_gain_mod = sum(p.moded_stat(stat + '_gain_mod', with_temp_checks = with_temp_checks) for p in self.other_people_in_room)

                # Returning chage result
                return self.delta_stat(stat, delta_value + self_stat_gain_mod + location_stat_gain_mod + people_stat_gain_mod, show_numbers, inverse, with_message, with_notify, reason)
            else:
                return self.delta_stat(stat, delta_value, show_numbers, inverse, with_message, with_notify, reason)

        def get_menu_objects(self, in_context):
            return self.get_evaled_actions(in_context)
    """
    The Person class handles both clients and minor characters
    prefix and suffix are used to get full_name using name_scheme
    pay is how much this client pays for week
    Add stats you want at the end
    """
    class Person(Talkative):
        def __init__(self, character, short_name, cut_portrait = True, prefix = "", suffix = "", name_scheme = "[prefix] [name] [suffix]", pay = 25, training_regime = 'weekly', available_on_weekends = True, trigger_phrase = "", available_trigger_phrases = [], week_available = 0, prospect_min_reputation = 0, **stats):
            Talkative.__init__(self, character, short_name, cut_portrait, **stats)
            self.prefix = prefix
            self.suffix = suffix
            self.name_scheme = name_scheme
            self.pay = pay
            self.training_regime = training_regime
            self.available_on_weekends = available_on_weekends
            self.available_trigger_phrases = available_trigger_phrases
            self.trigger_phrase = trigger_phrase
            self.week_available = week_available
            self.prospect_min_reputation = prospect_min_reputation
            self.show_in_statblock = ['sos', 'desire', 'submission', 'resistance']
            self.remove_tags_daily = {'trained_today'}
            self.remove_tags_weekly = { 'trained_this_week', 'will_tamer_this_week' } # This is a set
            self.is_prospect = False
            self.hypno_ratios = {}

            self.status = 'minor_character'
            self.current_note = None
            all_minor_characters.append(self)

            # Adding Stats that may be missing
            self.transformed_via_object = False
            self.fixed_location = None
            self.add_stats_with_value('sos', 'desire', 'submission', 'hypno_sessions_this_week', 'hypno_count', 'min_reputation', 'hypno_trigger_resistance_threshold', 'visit_count', 'visit_count_total', 'temporary_count', 'sex_count', 'anal_count', 'spank_count', 'pleasure_her_count', 'masturbation_count', 'blowjob_count', 'swallow_count', 'facial_count', 'orgasm_count', 'dommed_count', 'stripped_count', 'handjob_count', 'titfuck_count', 'footjob_count', 'will_tamer_count', 'hypno_handjob_count', 'hypno_blowjob_count', 'hypno_titfuck_count', 'hypno_sex_count', 'hypno_anal_count', 'hypno_orgasm_count', 'hypno_swallow_count', 'hypno_facial_count')
            self.add_stats(resistance = 100, hypno_trigger_level_threshold = 10, training_period = 12, wait_for_message_period = 4, hypno_trigger_sessions_threshold = 8)

            self.examine_action = self.add_action("^'Examine ' + this.name", label = "_examine", this = self, unseen = False, seen_result = True)

            # Hypnosis General
            self.hypno_action = self.add_action("Hypnosis", label = "_hypnosis_start", new_context = "_hypnosis", condition = "player.moded_stat('hypnosis_level', with_temp_checks = False) > 0 and client.can_be_hypno and client.can_be_interacted", client = self, locked_menu = True)

        def add_hypno_actions(self, stats_list = ['sos', 'desire', 'submission', 'resistance'], implant = True, custom_implant = True):
            if implant:
                self.implant_action = self.add_action("Implant Trigger", label = "implant_hypnosis_action_label", context = "_hypnosis", condition = 'client.can_receive_trigger[0]', client = self)

            if stats_list:
                for stat in stats_list:
                    self.__dict__[stat + "_hypno_action"] = self.add_action("Change " + stats[stat], label = "hypnosis", context = '_hypnosis', stat = stat, custom_implant = custom_implant)

        # This returns the full name using name_scheme
        @property
        def full_name(self):
            return self.name_scheme.replace('[prefix]', self.prefix).replace('[name]', self.name).replace('[suffix]', self.suffix).strip()

        # Returns the week in which training ends
        @property
        def training_limit(self):
            return self.stats['training_period'] + week - 1

        @property
        def accept_limit(self):
            return self.stats['wait_for_message_period'] + week

        # Return True if the curren location is this location
        @property
        def is_here(self):
            return current_location == self.location

        @property
        def can_be_interacted(self):
            # Unavailable clients are not interactable
            if self.status == 'unavailable':
                return False

            # Every client should be interactable on weekends
            if self.status == 'on_training' and day == 5:
                return self.available_on_weekends

            # Other days we check the regime
            if self.training_regime == 'weekly':
                return 'trained_this_week' not in self.tags
            elif self.training_regime == 'daily':
                return 'trained_today' not in self.tags

            return True

        # Return if the player has hypno sessions left for this client
        @property
        def can_be_hypno(self):
            return player.stats['max_weekly_hypno_sessions_per_person'] > self.stats['hypno_sessions_this_week'] and 'no_hypnosis' not in self.tags

        @property
        def can_receive_trigger(self):
            reasons = []
            if not renpy.has_label(self.short_name + "_implant_trigger"):
                reasons.append('label')

            if self.hypno_count < self.hypno_trigger_sessions_threshold:
                reasons.append('sessions')

            if player.hypnosis_level < self.hypno_trigger_level_threshold:
                reasons.append('level')

            if self.resistance > self.hypno_trigger_resistance_threshold:
                reasons.append('resistance')

            if 'trigger_implanted' in self.tags:
                reasons.append('implanted')

            if 'implant_trigger_failed' in self.tags:
                reasons.append('failed')

            return (len(reasons) == 0, reasons)

        # Generates the stat_block fof the examine label
        @property
        def statblock(self):
            sblock = "You sense her:\n"

            for stat in self.show_in_statblock:
                sblock += "{} is : {}{}\n".format(stats[stat], self.stat_to_text(stat), " (" + str(self.stats[stat]) + ")" if player.has_tag("show_" + stat) else "")

            return sblock

        # Converts a stat to text as in the game
        def stat_to_text(self, stat):
            num = self.stats[stat]
            if num > 60:
                color = '#090' if stat not in inverse_stats else '#F00' #trying darker green
                # color = '#0F0' if stat not in inverse_stats else '#F00' #original lime green
            elif num <= 40:
                color = '#F00' if stat not in inverse_stats else '#090' #trying darker green
                # color = '#F00' if stat not in inverse_stats else '#0F0' #original lime green
            else:
                color = '#FFF'

            if num < 0:
                text = "Extremely Low"
            elif num <= 20:
                text = "Very Low"
            elif num <= 40:
                text = "Low"
            elif num <= 60:
                return "Moderate"
            elif num <= 80:
                text = "High"
            elif num <= 100:
                text = "Very High"
            else:
                text = "Extremely High"

            return "{color=" + color + "}" + text + "{/color}"

        # Allows changing prefix, name and suffix
        def change_full_name(self, prefix="", name="", suffix=""):
            self.name = name
            self.prefix = prefix
            self.suffix = suffix

        def change_status(self, status):
            statuses = ['minor_character', 'prospect', 'rejected', 'available_to_be_client', 'waiting_on_message', 'on_training', 'post_training', 'unavailable']
            if status not in statuses:
                renpy.error("The requested status doesn't exists.")
                return

            original_status = self.status

            while self.status != status:

                if statuses.index(self.status) < statuses.index(status): # Going up!
                    # Next status on the list
                    self.status = statuses[statuses.index(self.status) + 1]

                    if original_status == 'minor_character' and status == 'prospect':
                        self.is_prospect = True

                    elif self.status == "rejected":
                        if original_status != 'prospect':
                            self.is_prospect = False

                        if not self.is_prospect:
                            all_minor_characters.remove(self)
                            all_clients.append(self)

                    elif self.status == "available_to_be_client":
                        pass

                    elif self.status == "waiting_on_message":
                        self.current_client_action = starting_location.add_action("New Message (Rep: {})".format("{image=gui/button/star.png}" * int(self.min_reputation + 1)), label = self.short_name + "_message", context = '_check_messages')

                    elif self.status == "on_training":
                        if self.is_prospect:
                            self.is_prospect = False
                            all_minor_characters.remove(self)
                            all_clients.append(self)
                        remove_note(self.current_note)
                        self.current_note = add_note(self.training_limit * 5, "{} training ends".format(self.name))
                        starting_location.remove_action(self.current_client_action)
                        self.current_client_action = starting_location.add_action("^ 'Call ' + client.full_name", label = self.short_name + "_calling", context = "_call_clients", condition = "client.can_be_interacted", client = self)
                        self.review_client_action = starting_location.add_action("^ 'Review ' + client.name", label = self.short_name + "_review_files", context = "_review_files", condition = "'first_visit' not in client.tags", client = self)

                    elif self.status == "post_training":
                        remove_note(self.current_note)
                        starting_location.remove_action(self.current_client_action)
                        self.current_client_action = starting_location.add_action("^ 'Contact ' + client.full_name", label = self.short_name + "_contact", context = "_post_training", condition = "client.can_be_interacted and not client.has_tag('post_continuing_actions')", client = self)

                    elif self.status == 'unavailable':
                        starting_location.remove_action(self.current_client_action)
                        starting_location.remove_action(self.review_client_action)
                        if 'relationship_action' in self.__dict__:
                            bedroom.remove_action(self.relationship_action)

                elif statuses.index(self.status) > statuses.index(status): # Going down!
                    # Previous status on the list
                    self.status = statuses[statuses.index(self.status) - 1]

                    if self.status == "minor_character":
                        if not self.is_prospect:
                            all_minor_characters.append(self)
                            all_clients.remove(self)
                        self.is_prospect = False

                    elif self.status == "prospect":
                        if not self.is_prospect and status == 'prospect':
                            self.is_prospect = True
                            all_minor_characters.append(self)
                            all_clients.remove(self)

                    elif self.status == "rejected":
                        pass

                    elif self.status == "available_to_be_client":
                        if not self.is_prospect:
                            all_clients.append(self)
                        starting_location.remove_action(self.current_client_action)
                        self.current_client_action = None

                    elif self.status == "waiting_on_message":
                        starting_location.remove_action(self.current_client_action)
                        starting_location.remove_action(self.review_client_action)
                        self.current_client_action = starting_location.add_action("New Message", label = self.short_name + "_message", context = '_check_messages')

                    elif self.status == "on_training":
                        if 'relationship_action' in self.__dict__:
                            bedroom.remove_action(self.relationship_action)
                        starting_location.remove_action(self.current_client_action)
                        self.current_client_action = starting_location.add_action("Call " + self.full_name, label = self.short_name + "_calling", new_context = "location", context = "_call_clients", condition = "client.can_be_interacted", client = self)
                        self.review_client_action = starting_location.add_action("Review " + self.name, label = self.short_name + "_review_files", context = "_review_files")

                    elif self.status == 'post_training':
                        self.current_client_action = starting_location.add_action("Contact " + self.full_name, label = self.short_name + "_contact", context = "_post_training", condition = "client.can_be_interacted", client = self)
                        self.relationship_action = bedroom.add_action("[self.full_name]", label = self.short_name + "_relationship_status", context = "_relationship_status", client = self)

        def dismiss(self, hide_image = True):
            if self.location:
                self.location.people.remove(self)

            self.remove_tag('follows')

            if hide_image:
                renpy.hide_screen('trainee_image')

            reset_menu()

        def training_session(self, daily_tag = True, weekly_tag = True):
            if daily_tag:
                self.add_tag('trained_today')

            if weekly_tag:
                self.add_tag('trained_this_week')

        def clear_training_session(self, daily_tag = True, weekly_tag = True):
            if daily_tag:
                self.remove_tag('trained_today')

            if weekly_tag:
                self.remove_tag('trained_this_week')

        # Add a hypno session this client
        def hypno_session(self, charge_energy = True):
            self.hypno_sessions_this_week += 1
            self.hypno_count += 1
            player.hypno_action_count += 1

            if charge_energy:
                player.change_stat('energy', -energy_hypnosis.value, with_notify = True, reason = 'Hypnosis')

        """
        Shows a selection of people based on status and tags, there needs to be a specific label or a default one (both mentioned below) for the person to appear on the choice list
        After selecting the client it tries to call self.short_name + '_' + selected.short_name + '_' + suffix
          if it can't find that label it tries for self.short_name + '_default_' + suffix as a fallback
        Mind that calling variable_scene within a python blocks will terminate its execution.
        """
        def variable_scene(self, suffix, with_status = None, tagged_with_any = [], tagged_with_all = [], not_tagged_with_any = []):

            choices = [(p.name, p) for p in get_people(with_status = with_status, tagged_with_any = tagged_with_any, tagged_with_all = tagged_with_all, not_tagged_with_any = not_tagged_with_any) if renpy.has_label(self.short_name + "_" + p.short_name + "_" + suffix) or renpy.has_label(self.short_name + "_default_" + suffix)] + [("Cancel", False)]

            person = False
            if len(choices) > 1:
                person = renpy.display_menu(choices)

            if person:
                if renpy.has_label(self.short_name + "_" + person.short_name + "_" + suffix):
                    renpy.call(self.short_name + "_" + person.short_name + "_" + suffix)
                else:
                    renpy.call(self.short_name + "_default_" + suffix, person = person)
            else:
                renpy.return_statement()

    ####
    # Player Section
    ####

    class TrainerType(Actionable):
        def __init__(self, name, short_name, bg = 'tp_bg_generic', label = "_introduction", chosen_label = None, tags = [], **stats):
            Actionable.__init__(self, short_name)
            self.name = name
            self.bg = bg
            self.label = self.short_name + label if label.startswith("_") else label
            self.chosen_label = self.short_name + chosen_label if chosen_label is not None and chosen_label.startswith("_") else chosen_label
            self.add_stats(**stats)
            self.tags = set(tags)

            all_trainer_categories.append(self)

    class Player(Talkative):
        def __init__(self, character):
            Talkative.__init__(self, character, short_name = 'replace_this')
            self.bg = 'tp_bg_generic'
            self.category_name = None
            self.orgasm_text = "Aaaggghhhh!!"

            # Stats
            self.add_stats_with_value('sos_mod', 'desire_mod', 'submission_mod', 'resistance_mod', 'sos_gain_mod', 'desire_gain_mod', 'submission_gain_mod', 'resistance_gain_mod', 'hypnosis_level', 'hypno_action_count', 'sos_action_count', 'desire_action_count', 'submission_action_count', 'resistance_action_count', 'whore_income', 'domme_income', 'investment_income', 'orgasm_count', 'lesbian_count', 'slavegirl_count', 'petgirl_count', 'girlfriend_count', 'showgirl_count', 'bimbo_count', 'assistant_count', 'teaching_aide_count', 'whore_count', 'degraded_count', 'adult_baby_count', 'doll_count', 'domme_count', 'satisfied_client_count', 'hypno_girlfriend_count', 'new_people_count', 'virgin_count', 'sr_visit_count', 'extra_clients_fee_this_week', 'handjob_count_total', 'blowjob_count_total', 'titfuck_count_total', 'sex_count_total', 'anal_count_total', 'orgasm_count_total', 'swallow_count_total', 'facial_count_total', 'hypno_handjob_count_total', 'hypno_blowjob_count_total', 'hypno_titfuck_count_total', 'hypno_sex_count_total', 'hypno_anal_count_total', 'hypno_orgasm_count_total', 'hypno_swallow_count_total', 'hypno_facial_count_total')
            self.add_stats(max_weekly_hypno_sessions_per_person = 1, training_slots = 3)
            self.add_stat('money', 100, min = 0)
            self.add_stat('energy', 100, min = 0, max = 100)
            self.add_stat('reputation', -1, min = -1)

            self.add_tags("show_energy", "show_reputation", "show_money")

            # Fallback kick out of the house
            self.fallback_kick_out_action = self.add_action("Fallback Kick Out", label = "kickout", condition = "client_in_fallback_condition()")

        # Hypnsis composite method
        def can_hypno(self, target):
            return target.can_be_hypno and player.test('hypnosis_level', 0)

        # We copy over all data from the category: names, tags, items, actions(?) and stats
        # No idea if category driven only actions can be useful, but might as well allow them
        # Added items so you can create categories that start with certain items
        def assign_category(self, category):
            self.category_name = category.name
            self.bg = category.bg
            self.short_name = category.short_name
            self.tags |= category.tags
            self.actions.extend(category.actions)

            # UI
            self.has_portrait_image = renpy.has_image(self.short_name + "_portrait")
            self.portrait = self.short_name + "_portrait" if self.has_portrait_image else None
            self.image = self.short_name + "_image"

            # Adding actions
            self.add_button("Player Actions", new_context = "_top_menu", auto_image = "gui/button/self_%s.png", button_weight = 5)
            self.examine_action = self.add_action("Examine Yourself", label = "examine_self", unseen = False, seen_result = True)
            self.concepts_action = self.add_action("Game Concepts", label = "concepts_help_menu", unseen = False, seen_result = True)
            self.inventory_action = self.add_button("Inventory", new_context = 'inventory', auto_image = "gui/button/inventory_%s.png", button_weight = 4)
            self.inventory_action.unseen = False

            # Writing over stats, or adding new stats if needed
            self.stats.update(category.stats)

            # Writing over actions
            for action in self.actions + self.buttons:
                if action.label.startswith('replace_this'):
                    action.label = action.label.replace('replace_this', self.short_name)
                if action.context.startswith('replace_this'):
                    action.context = action.context.replace('replace_this', self.short_name)
                if action.new_context.startswith('replace_this'):
                    action.new_context = action.new_context.replace('replace_this', self.short_name)
