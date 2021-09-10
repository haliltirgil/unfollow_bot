from instapy import InstaPy

session = InstaPy(username='XXXXXXX', password='XXXXXXX',
                  headless_browser=False)

session.login()


session.unfollow_users(amount=1000,
                       allFollowing=True,
                       unfollow_after=0,
                       sleep_delay=601)

session.end()
