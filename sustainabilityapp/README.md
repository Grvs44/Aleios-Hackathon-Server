# `sustainabilityapp` Django app
## `admin.py`
- Registers each of the models from `models.py` so they are visible in the Django Site Admin

## `filters.py`
- Custom filters used by viewsets in `views.py` to allow filtering database queries

## `models.py`
- `category_choices` is the set of available categories for `Post`s and `Tag`s
- `User`
  - Extends and replaces the default `User` model
  - `join_date` is set when a `User` object is created and is then read-only
  - `bio` is an optional short description of the user
  - `score` is the sustainability score of the user (not implemented). Defaults to 0 as the starting score
  - `interested` is a many-to-many relationship with the `Post` model managed by Django which is rendered in the API as a list of all the `Post`s the user has said they are interested in
- `Tag`
  - `category` is a choice from a set of categories, for the different types of posts
    - A feature yet to be implemented is validation to make sure a `Post` only has `Tag`s that have its category
  - `name` is the display name of the `Tag`
- `Post`
  - `owner` is the `User` who created the `Post`
  - `category` is the choice from a set of categories (same as `Tag.category`)
  - `description` is the text displayed on the `Post`
  - `post_time` is the creation date and time of the `Post`; it is read-only
  - `modified_time` is the date and time of when the `Post` was last saved, it can only be modified by the Django ORM
  - `start_time` is edited by the user, and not compulsory. It is the date and time of
    - when the event starts, if it is an event
    - when the user is ready to give away the item/food, otherwise  
  - `end_time` is edited by the user, and not compulsory. It is the date and time of
    - when the event ends, if it is an event
    - when the user is no longer able to give away the item, if it is an item
    - when the food item has expired, if it is a food item
  - `tags` is a many-to-many relationship with the `Tag` model managed by Django which is rendered in the API as a list of all the `Tag`s that have been linked with the `Post`
- `Comment`
  - `post` is the `Post` object that this `Comment` is for
  - `owner` is the `User` object that created this `Comment`
  - `text` is what the user has written in the `Comment`
  - `post_time` is the creation date and time of the `Comment`; it is read-only
- `Image`
  - `post` the `Post` object that the `Image` is part of (a `Post` can have many `Image`s)
  - `alt_text` is the alternative text for the `Image`, displayed if the picture can't be displayed or read out in screen-readers
  - `image` stores the path of the image in the database, but provides a file upload interface to the user (that only accepts image format)
    - The image file is uploaded to the `MEDIA_ROOT` defined in `settings.py`

## `permissions.py`
- `IsOwner`
  - Allows anyone to view a `User` object, but only that user can modify/delete it (their account)
- `IsPostOwner`
  - Allows anyone to view a `Post` object, but only the user that created it can modify/delete it
- `IsImageOwner`
  - Allows anyone to view an `Image` object, but only the user that created the `Post` that it is linked to can modify/delete it
- `IsCommentOwner`
  - Allows anyone to view a `Comment` object, but only the user that created it can modify/delete it

## `serializers.py`
- `PostSerializer`
  - Uses all the fields in the `Post` model to serialize/deserialize JSON
- `ImageSerializer`
  - Uses all the fields in the `Image` model to serialize/deserialize JSON
- `CommentSerializer`
  - Uses all the fields in the `Comment` model to serialize/deserialize JSON
- `TagSerializer`
  - Uses the `id` and `name` fields in the `Tag` model to serialize/deserialize JSON
- `UserSerializer`
  - Uses the `id`, `first_name`, `last_name`, `username`, `password`, and `interested` fields in the `User` model to serialize/deserialize JSON
  - When the user is created, the value passed in as the password is given to the `set_password` method, so the password is stored correctly (ie the hash instead of plaintext)

## `urls.py`
- Includes all the URL patterns of the API (see the API documentation in `/README.md`)
- Includes the URL patterns for the `knox` package (which manages `TokenAuthentication`) individually
  - This was because the `LoginView` needed to be modified - see `views.LoginView`
- Statically serves the `MEDIA_ROOT` folder at `MEDIA_URL` (both defined in `/hackathon/settings.py`), but only when `DEBUG = True`

## `views.py`
- `UserViewSet`, `PostViewSet`, `ImageViewSet`, `CommentViewSet`, and `TagViewSet` provides the set of CRUD APIs to the corresponding model
- Attributes
  - `queryset`: the object that represents the starting point of any query
  - `serializer_class`: the serializer class used for serializing/deserializing JSON
  - `permission_classes`: a list/tuple of the classes that can manage permissions (for list, and for objects)
  - `authentication_classes`: a list/tuple of the authentication requirements of users to have access to the viewset
  - `filter_backends`: a list/tuple of filter classes that can apply further filters to the `queryset`
  - `filterset_fields`: a list/tuple of the fields that can be used for filtering by the filter classes in `filter_backends`
- `LoginView`
  - Overrides the default `knox.views.LoginView` and modifies the `get_post_data_response` method so the `id` and `first_name` of the `User` object are also returned
