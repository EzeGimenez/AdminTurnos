package com.adminturnos.Database;

import com.adminturnos.UserManagment.UserManagment;
import com.loopj.android.http.AsyncHttpClient;
import com.loopj.android.http.RequestParams;

import java.util.Map;

/**
 *
 */
public class DatabaseDjangoRead implements DatabaseRead {

    private static DatabaseDjangoRead instance;
    private static AsyncHttpClient client;
    private static Database database;

    /**
     * Default constructor
     */
    private DatabaseDjangoRead() {
        database = new DatabaseDjango();
        client = new AsyncHttpClient();
        client.addHeader("Authorization", "Token " + UserManagment.getInstance().getAccessToken());
    }

    public static DatabaseDjangoRead getInstance() {
        if (instance == null) {
            instance = new DatabaseDjangoRead();
        }
        return instance;
    }

    @Override
    public void GET(String subDirURL, Map<String, String> body, DatabaseCallback callback) {

        RequestParams params = new RequestParams();
        if (body != null) {
            for (Map.Entry<String, String> entry : body.entrySet()) {
                params.put(entry.getKey(), entry.getValue());
            }
        }

        String url = database.getUrl() + subDirURL;
        client.get(
                url,
                params,
                callback
        );
    }

}