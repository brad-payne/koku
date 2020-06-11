/*
Copyright 2020 Red Hat, Inc.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */
-- Function to generate a sha256 hash from the concatenation
-- of all of the text values passed into the function
create or replace function {schema_name}.koku_record_uuid ( VARIADIC vals text[] ) returns uuid as
$$
declare
    -- The string of the concatenation of the parameter values
    record_val text = ''::text;
    -- The output UUID
    return_val uuid = null::uuid;
    -- Iterator var
    i int = 1::int;
begin
    -- Loop over the parameter values, concatenating them together
    for i in 1 .. array_upper(vals, 1)
    loop
        -- Translate nulls to empty string
        if vals[i] is null
        then
            vals[i] = '';
        end if;
        record_val = record_val || vals[i];
    end loop;

    -- If all values end up generating an empty string, return null
    if record_val = ''
    then
        return_val = null::uuid;
    else
        -- Otherwise generate a UUID5
        select public.uuid_generate_v5(public.uuid_ns_oid(), record_val) into return_val;
    end if;

    return return_val;
end;
$$
language plpgsql
returns null on null input;