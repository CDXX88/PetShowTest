import os
class Urls:

    stage = os.getenv('STAGE', 'REMOTE').upper()

    if stage == 'DOCKER':
        base_url = 'http://localhost:8080/api/v3'
    elif stage == 'REMOTE':
        base_url = 'https://petstore.swagger.io/v2'

    pet = '/pet' ## add a new pet to the store and update an existing pet, used in put_pet and post_pet
    pet_id = '/pet/' ## used in delete, update, get_by_id
    pet_find_by_status = '/pet/findByStatus' ## finds pets by status
    pet_upload_image = '/uploadImage' ## uploads and image
    pet_find_by_tags = '/pet/findByTags' ## searching pet by tag