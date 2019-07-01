from sdk.users import UserService


def run():
    print('Starting...')
    user_service = UserService()

    # listing all users
    users = user_service.list_all()

    # create an user   
    user_data = {
        'name': 'Armando',
        'age': 33
    }
    user_service.create(user_data)

    # modifying a user
    user_data['email'] = 'armando.miani@gmail.com'
    user_service.update(10, user_data)

    # listing on production
    user_service = UserService('prod')

    # listing all users
    users = user_service.list_all()


if __name__ == '__main__':
    run()
