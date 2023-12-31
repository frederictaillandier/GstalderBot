""" Test the message formater"""
import datetime
from srcs.message_formater import MessageFormater


def test_message_formating_of_role_change():
    """Test formater of the change of food master"""
    formater = MessageFormater("abc")
    assert (
        formater.get_role_update_text("123")
        == "123 is no more the food master. abc is the new food master.\n\n"
    )


def test_message_formating_of_weekly_schedule():
    """Test formater of the weekly schedule"""
    formater = MessageFormater("abc")
    message = formater.get_weekly_schedule_text(
        {datetime.datetime(2023, 6, 1): [0], datetime.datetime(2023, 6, 2): [1]}
    )
    assert (
        message
        == "Hello abc,\n"
        + "for this week you need to put these trashes in front the house before 7:00am:\n"
        + "The We recycle on Thursday.\n"
        + "The Normal on Friday.\n"
        + "Thank you !\n"
    )


def test_message_weekly_schedule_multiple_trash():
    """Test formater of the weekly schedule with multiple trash"""
    formater = MessageFormater("123")
    message = formater.get_weekly_schedule_text(
        {datetime.datetime(2023, 6, 1): [0, 1], datetime.datetime(2023, 6, 2): [1]}
    )
    assert (
        message
        == "Hello 123,\n"
        + "for this week you need to put these trashes in front the house before 7:00am:\n"
        + "The We recycle and Normal on Thursday.\n"
        + "The Normal on Friday.\n"
        + "Thank you !\n"
    )


def test_message_formating_of_daily_schedule():
    """Test formater of the daily schedule"""
    formater = MessageFormater("abc")
    message = formater.get_daily_update_text([0, 1])
    assert (
        message
        == "Hi abc! Don't forget to take out "
        + "the We recycle and Normal before 7am tomorrow.\n"
        + "Do we still have enough we-recycle bags ?\n"
        + "If not, can you order some new ? By adding a sticker on the last bag ?\n"
        + "Have a nice evening."
    )


def test_message_formating_of_daily_schedule_empty():
    """Test formater of the daily schedule as empty"""
    formater = MessageFormater("abc")
    message = formater.get_daily_update_text([])
    assert message == "Hi abc! No trash pickup for tomorrow, have a nice evening!\n\n"
