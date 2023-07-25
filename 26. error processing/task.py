# 1

def image_info(img):
    if 'image_title' not in img:
        raise TypeError("Dictionary have no 'image_title' key!")
    elif 'image_id' not in img:
        raise TypeError("Dictionary have no 'image_id' key!")
    return f"Image '{img['image_title']}' has id {img['image_id']}"

# def image_info(img):
    # if ('image_id' not in img) or ('image_title' not in img):
    #     raise TypeError("Keys image_id and image_title must be present")
    # return f"Image '{img['image_title']}' has id {img['image_id']}"


image_one = {
    'image_id': 5138,
    'image_title': 'my cat'
}

image_two = {
    # 'image_id': 5138,
    'image_title': 'my cat',
    'image_size': '800x600'
}

image_three = {
    'image_id': 5140,
    # 'image_title': 'my dog',
    'image_size': '800x600'
}

print(image_info(image_one))
try:
    print(image_info(image_three))
except TypeError as e:
    print(e)

# try:
#     image_info(image_three)
# except TypeError as e:
#     print(e)


# Решение
