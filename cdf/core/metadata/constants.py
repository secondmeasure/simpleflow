from enum import Enum


# Fields flags to return a specific field type rendering
class RENDERING(Enum):
    URL = 'url'
    IMAGE_URL = 'image_url'
    # Returns a 2-tuple list of (url, http_code)
    URL_HTTP_CODE = 'url_http_code'
    # Return a dict {"url": {"url": url, "crawled": bool_crawled}, "status": ["follow"]}
    URL_LINK_STATUS = 'url_link_status'
    # Return a dict {"url": url, "crawled": bool_crawled}
    URL_STATUS = 'url_status'
    # Returns a map dict:
    # {'text': ["My text", "My other text", ..], 'nb': [20, 10..]}
    STRING_NB_MAP = 'string_nb_map'
    DEPTH = 'depth'
    LINK = 'link'
    VISIT = 'visit'
    TIME_SEC = 'time_sec'
    TIME_MILLISEC = 'time_millisec'
    TIME_MIN = 'time_min'
    PERCENT = 'percent'
    HREFLANG_VALID_VALUES = 'hreflang_valid_values'
    HREFLANG_ERROR_VALUES = 'hreflang_error_values'
    NOT_SORTABLE = 'not_sortable'


# TODO(darkjh) separate this enum
#   - field has roles: filters, select etc
#   - field has its visibility: private, admin etc.
#   so they should go into 2 different enums
class FIELD_RIGHTS(Enum):
    # This field is private and cannot be requested outside
    PRIVATE = 'private'
    # This field is visible only to admin user
    ADMIN = 'admin'
    # This field can be called in filtering operations
    FILTERS = 'filters'
    # This field can be called in filtering operations
    # but just to check if it exists
    FILTERS_EXIST = 'filters_exist'
    # This field can only be selected for results
    SELECT = 'select'