package com.adminturnos.Activities.NewPlace;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

import com.adminturnos.Activities.ObjectConfigurator;
import com.adminturnos.R;
import com.google.android.material.checkbox.MaterialCheckBox;

public class NewPlaceEFragment extends ObjectConfigurator {

    private MaterialCheckBox checkBox;

    public NewPlaceEFragment() {

    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        return inflater.inflate(R.layout.fragment_new_place_e, container, false);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        this.checkBox = view.findViewById(R.id.checkboxNewPlace);
    }

    @Override
    public void setExtras(Bundle bundle) {

    }

    @Override
    public Bundle getData() {
        Bundle bundle = new Bundle();

        bundle.putBoolean("works_here", checkBox.isChecked());

        return bundle;
    }

    @Override
    public boolean validateData() {
        //TODO
        return true;
    }

}