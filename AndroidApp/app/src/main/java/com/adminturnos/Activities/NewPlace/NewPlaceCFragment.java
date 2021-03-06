package com.adminturnos.Activities.NewPlace;

import android.os.Bundle;
import android.text.TextUtils;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

import com.adminturnos.Activities.ObjectConfigurator;
import com.adminturnos.R;
import com.google.android.material.textfield.TextInputEditText;
import com.google.android.material.textfield.TextInputLayout;

public class NewPlaceCFragment extends ObjectConfigurator {

    TextInputEditText etPhone;

    public NewPlaceCFragment() {

    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        return inflater.inflate(R.layout.fragment_new_place_c, container, false);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        etPhone = view.findViewById(R.id.editTextPhone);
    }

    @Override
    public void setExtras(Bundle bundle) {

    }

    @Override
    public Bundle getData() {

        String phone = etPhone.getText().toString();
        Bundle bundle = new Bundle();
        bundle.putString("phonenumber", phone);

        return bundle;
    }

    @Override
    public boolean validateData() {
        TextInputLayout textInputLayout = getView().findViewById(R.id.text_input_layout_phone);
        if (TextUtils.isEmpty(etPhone.getText())) {
            textInputLayout.setError("Este campo es obligatorio");
            return false;
        } else {
            textInputLayout.setError(null);
        }

        return true;
    }

}