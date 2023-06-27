import pytest, datetime
from srcs.message_formater import MessageFormater

def test_message_formater_init():
    with pytest.raises(Exception):
        MessageFormater()

def test_message_formater_init_no_config():
    formater = MessageFormater("abc")
    assert formater.get_role_update_text("123") == "123 is no more the food master. abc is the new food master.\n\n"

def test_message_weekly_schedule():
    formater = MessageFormater("abc")
    message = formater.get_weekly_schedule_text({datetime.datetime(2023, 6, 1) : [0], datetime.datetime(2023, 6, 2):[1]})
    assert message == "Hello abc,\nfor this week you need to put these trashes in front the house before 7:00am:\nThe We recycle on Thursday.\nThe Normal on Friday.\nThank you !\n"

def test_message_weekly_schedule_multiple_trash():
    formater = MessageFormater("abc")
    message = formater.get_weekly_schedule_text({datetime.datetime(2023, 6, 1) : [0, 1], datetime.datetime(2023, 6, 2):[1]})
    assert message == "Hello abc,\nfor this week you need to put these trashes in front the house before 7:00am:\nThe We recycle and Normal on Thursday.\nThe Normal on Friday.\nThank you !\n"
