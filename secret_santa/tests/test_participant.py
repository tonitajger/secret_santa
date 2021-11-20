import pytest

from secret_santa.src.participant import Participant


class TestConstructor:
    def test_should_correctly_construct_participant_with_name_and_group(self):
        name = "some_name" 
        group = "some_group"
        giver = Participant(name="some_giver")
        receiver = Participant(name="some_receiver")
        p = Participant(name=name, group=group, giver=giver, receiver=receiver)

        assert p.name == name
        assert p.group == group
        assert p.giver == giver
        assert p.receiver == receiver

    def test_should_correctly_construct_participant_only_required_arguments(self):
        name = "some_name" 
        p = Participant(name=name)
        assert p.name == name
        assert p.group is None
        assert p.giver is None
        assert p.receiver is None


class TestIsDone:
    def test_should_consider_participant_with_giver_and_receiver_as_done(self):
        p = Participant(name="some_name")
        p.giver = Participant(name="some_name_1")
        p.receiver = Participant(name="some_name_2")

        assert p.is_done

    def test_should_consider_participant_without_giver_as_not_done(self):
        p = Participant(name="some_name")
        p.receiver = Participant(name="some_name_2")

        assert not p.is_done

    def test_should_consider_participant_without_receiver_as_not_done(self):
        p = Participant(name="some_name")
        p.giver = Participant(name="some_name_1")

        assert not p.is_done

    def test_should_consider_participant_without_giver_or_receiver_as_not_done(self):
        p = Participant(name="some_name")

        assert not p.is_done


class TestAssignGiver:
    def test_should_not_assign_giver_for_no_participants(self):
        p = Participant(name="some_name")

        assert p.assign_giver([]) is None
        assert p.giver is None

    def test_should_not_assign_itself_as_giver(self):
        p = Participant(name="some_name")
        participants = [Participant(name="some_name")]
        
        assert p.assign_giver(participants) is None
        assert p.giver is None

    def test_should_not_assign_participant_from_same_group_as_giver(self):
        p = Participant(name="some_name", group="some_group")
        participants = [Participant(name="some_other_name", group="some_group")]
        
        assert p.assign_giver(participants) is None
        assert p.giver is None

    def test_should_not_assign_giver_if_has_giver(self):
        p = Participant(name="some_name")
        giver = Participant(name="some_other_name_1")
        receiver = Participant(name="some_other_name_2")
        giver.receiver = receiver
        participants = [giver]
        
        assert p.assign_giver(participants) is None
        assert p.giver == None

    def test_should_not_assign_giver_if_giver_has_receiver(self):
        p = Participant(name="some_name")
        giver = Participant(name="some_other_name_1")
        p.giver = giver
        participants = [Participant(name="some_other_name_2")]
        
        assert p.assign_giver(participants) is None
        assert p.giver == giver

    def test_should_not_assign_giver_if_is_receiver(self):
        p = Participant(name="some_name")
        giver = Participant(name="some_other_name_1")
        participants = [giver]
        p.receiver = giver
        
        assert p.assign_giver(participants) is None
        assert p.giver is None

    @pytest.mark.parametrize(
        "current, giver",
        [
            (
                Participant(name="some_name", group="some_group"), 
                Participant(name="some_other_name", group="some_other_group")
            ),
            (
                Participant(name="some_name"), 
                Participant(name="some_other_name", group="some_other_group")
            ),
            (
                Participant(name="some_name", group="some_group"), 
                Participant(name="some_other_name")
            ),
            (
                Participant(name="some_name"), 
                Participant(name="some_other_name")
            ),
            (
                Participant(name="some_name", group="some_group", receiver=Participant("some_name_other_1")), 
                Participant(name="some_other_name", group="some_other_group", giver=Participant("some_name_other_1"))
            ),
            (
                Participant(name="some_name", group="some_group", receiver=Participant("some_name_other_1")),
                Participant(name="some_other_name", group="some_other_group")
            ),
            (
                Participant(name="some_name", group="some_group"),
                Participant(name="some_other_name", group="some_other_group", giver=Participant("some_name_other_1"))
            ),
        ]
    )
    def test_should_correctly_assign_giver_for_valid_cases(self, current, giver):
        assert current.assign_giver([giver]) == giver
        assert current.giver == giver
        assert giver.receiver == current
