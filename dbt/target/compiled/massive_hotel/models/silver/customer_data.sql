






    



select 

    record_content:address.streetAddress as address_streetAddress, 

    record_content:created_at as created_at, 

    record_content:first_name as first_name, 

    record_content:id as id, 

    record_content:last_name as last_name, 

    record_content:phone_number[0].number as phone_number_0_number, 

    record_content:phone_number[0].type as phone_number_0_type, 

    record_content:phone_number[2].type as phone_number_2_type, 

    record_content:middle_name as middle_name, 

    record_content:phone_number[2].number as phone_number_2_number, 

    record_content:updated_at as updated_at, 

    record_content:address.city as address_city, 

    record_content:address.country as address_country, 

    record_content:address.postalCode as address_postalCode, 

    record_content:age as age, 

    record_content:email as email, 

    record_content:phone_number[1].number as phone_number_1_number, 

    record_content:phone_number[1].type as phone_number_1_type, 

    record_content:phone_number[3].number as phone_number_3_number, 

    record_content:phone_number[3].type as phone_number_3_type


from massive_hotel.bronze.customer_raw_data



  -- this filter will only be applied on an incremental run
  -- (uses >= to include records with updated at greater than data currently present in silver layer)
  where record_content:updated_at >= (select max(updated_at) from massive_hotel.silver.customer_data)
