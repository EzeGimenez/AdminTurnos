package com.adminturnos;

public interface Values {

    /* USER MANAGEMENT */
    int RC_SIGN_UP = 1;
    int RC_SIGN_IN_ACTIVITY = 2;
    int RC_NEW_PLACE = 3;

    /* Shared Preferences */
    String SHARED_PREF_NAME = "SharedPref";
    String SHARED_PREF_ACCESS_TOKEN = "AccessToken";

    /* Google Console */
    String CLIENT_ID_WEB_APP = "237762704075-uokqack5o2rdqd2ju15uprcc2ttkoo5j.apps.googleusercontent.com";

    /* Django URL */
    String DJANGO_URL_BASE = "http://192.168.1.50:8000";
    String DJANGO_URL_CONVERT_TOKEN = "/auth/login-android-google/";
    String DJANGO_URL_GET_JOBS = "/android/profile/jobs/";
    String DJANGO_URL_GET_OWNED_PLACES = "/android/profile/places/";
    String DJANGO_URL_NEW_PLACE = "/android/new-place/";
    String DJANGO_URL_JOBTYPES = "/android/jobtypes/";
    String DJANGO_URL_PLACE_DOES = "/android/profile/place-does/";
    String DJANGO_URL_JOB_REQUEST = "/android/profile/job-requests/";
    String DJANGO_URL_ACCEPT_JOB_REQUEST = "/android/profile/accept-job-request/";
    String DJANGO_URL_CANCEL_JOB_REQUEST = "/android/profile/cancel-job-request/";
    String DJANGO_URL_SEARCH_PLACE = "/android/search-place/";
    String DJANGO_URL_NEW_JOB_REQUEST = "/android/new-job-request/";
    String DJANGO_URL_GET_APPOINTMENTS = "/android/get-appointments/";
}
