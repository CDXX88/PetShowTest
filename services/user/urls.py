class Urls:

    base_url = 'https://petstore.swagger.io/v2'

    user = '/user' ## create user
    user_with_array = '/user/createWithArray' ## create list of users with given input array
    user_login = '/user/login' ## logs user into the system
    user_logout = '/user/logout' ## logs out current logged-in user session
    user_by_username = '/user/' ## add {username} in the end of url, used in delete_user, update_user, get_user_by_username