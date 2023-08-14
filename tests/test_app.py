from playwright.sync_api import Page, expect
from datetime import datetime

# Tests for your routes go here

# === Example Code Below ===

'''
Test Chitter homepage has title, list of archive peeps and text 'login'.
'''
def test_get_homepage(page, test_web_address, db_connection):
    db_connection.seed("seeds/chitter.sql")
    page.goto(f"http://{test_web_address}/")
    header_tag = page.locator(".t-header")
    archive_tag_1 = page.locator(".t-archive").nth(1)
    archive_tag_2 = page.locator(".t-archive").nth(2)
    archive_tag_3 = page.locator(".t-archive").nth(3)
    login_tag = page.locator(".t-login")
    expect(header_tag).to_have_text("chitter")
    expect(archive_tag_1).to_have_text("Peep by telon_tusk (Telon Tusk) at 17:20 on 24/05/23: Now you guys are just being rude.")
    expect(archive_tag_2).to_have_text('Peep by telon_tusk (Telon Tusk) at 12:12 on 23/05/23: Wow, my peep is lonely, and so am I!')
    expect(archive_tag_3).to_have_text('Peep by telon_tusk (Telon Tusk) at 12:00 on 23/05/23: Just reset chitter...')
    expect(login_tag).to_have_text("Login")

'''
Test valid login goes to user page, with create peep form, creates new peeps and shows user's peeps.

############ Not yet added:
tagged peeps 
'''
def test_valid_login(page, test_web_address, db_connection):
    db_connection.seed("seeds/chitter.sql")
    page.goto(f"http://{test_web_address}/")
    page.fill("input[name=user_handle]", "telon_tusk")
    page.fill("input[name=user_password]", "NooneWillGuessMe")
    page.click("text='Login'")
    header_tag = page.locator(".t-header")
    expect(header_tag).to_have_text("chitter")
    user_tag = page.locator(".t-user")
    expect(user_tag).to_have_text("telon_tusk (Telon Tusk)")
    page.fill("input[name=content]", "Hello my only friend.")
    page.fill("input[name=tags]", "no_vowel_bot")
    post_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    page.click("text='Peep'")  
    archive_tag_1 = page.locator(".t-archive").nth(0) 
    expect(archive_tag_1).to_have_text(f"Peep by telon_tusk (Telon Tusk) at {post_time[11:16]} on {post_time[0:6]}{post_time[8:10]}: Hello my only friend. #no_vowel_bot") 

'''
Test invalid login rejects with appropriate messages.
'''
def test_invalid_login(page, test_web_address, db_connection):
    db_connection.seed("seeds/chitter.sql")
    page.goto(f"http://{test_web_address}/")
    page.click("text='Login'")
    errors_tag = page.locator(".t-errors")
    expect(errors_tag).to_have_text("Username missing. Password missing. ")
    page.fill("input[name=user_handle]", "telon_tusk")
    page.fill("input[name=user_password]", "Noonee")
    page.click("text='Login'")
    header_tag = page.locator(".t-header")
    expect(header_tag).to_have_text("chitter")
    expect(errors_tag).to_have_text("Incorrect password. ")
    page.fill("input[name=user_handle]", "telom_tusp")
    page.fill("input[name=user_password]", "NooneWillGuessMe")
    page.click("text='Login'")
    expect(errors_tag).to_have_text("Incorrect username. ")

'''
Test post tweet from user page when not logged in returns error.
'''
def test_invalid_login(page, test_web_address, db_connection):
    db_connection.seed("seeds/chitter.sql")
    #page.goto(f"http://{test_web_address}/user/telon_tusk")
    #page.goto("http://localhost:5000/user/telon_tusk")
    page.goto(f"http://{test_web_address}/user/no_vowel_bot")
    header_tag = page.locator(".t-header")
    expect(header_tag).to_have_text("chitter")
    user_tag = page.locator(".t-user")
    expect(user_tag).to_have_text("telon_tusk (Telon Tusk)")
    page.fill("input[name=content]", "Hello my only friend.")
    page.fill("input[name=tags]", "no_vowel_bot")
    page.click("text='Login'")
    errors_tag = page.locator(".t-errors")
    expect(errors_tag).to_have_text("You must log in to peep and peep from your user page. ")

'''
Test log out button send user to homepage.
'''

'''
Test logging in logs out previously logged in user.
'''

'''
Test peep must have content but can have empty tags.
'''

# === End Example Code ===
