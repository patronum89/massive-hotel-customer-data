
  
    

        create or replace transient table massive_hotel.silver.staging_customer_data
         as
        (






    
    


select 

    record_content:address.country::STRING as address_country, 

    record_content:address.streetAddress::STRING as address_streetAddress, 

    record_content:first_name::STRING as first_name, 

    record_content:phone_number[0].type::STRING as phone_number_0_type, 

    record_content:phone_number[2].number::NUMBER as phone_number_2_number, 

    record_content:address.city::STRING as address_city, 

    record_content:last_name::STRING as last_name, 

    record_content:phone_number[3].number::NUMBER as phone_number_3_number, 

    record_content:phone_number[2].type::STRING as phone_number_2_type, 

    record_content:id::NUMBER as id, 

    record_content:phone_number[0].number::NUMBER as phone_number_0_number, 

    record_content:phone_number[1].number::NUMBER as phone_number_1_number, 

    record_content:phone_number[3].type::STRING as phone_number_3_type, 

    record_content:email::STRING as email, 

    record_content:address.postalCode::NUMBER as address_postalCode, 

    record_content:age::NUMBER as age, 

    record_content:created_at::STRING as created_at, 

    record_content:middle_name::STRING as middle_name, 

    record_content:phone_number[1].type::STRING as phone_number_1_type, 

    record_content:updated_at::STRING as updated_at


from massive_hotel.bronze.customer_raw_data



        );
      
  