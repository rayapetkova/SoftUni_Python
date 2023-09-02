create or replace function fn_full_name(first_name text, last_name text)
returns text
language plpgsql
as
$$
declare
   full_name text;
begin
   full_name := CONCAT(first_name, ' ', last_name);
   return INITCAP(full_name);
end;
$$;