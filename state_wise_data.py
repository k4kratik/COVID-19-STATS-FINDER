def get_state_data(driver):

    driver.get("https://zeenews.india.com/coronavirus-news/statewise")

    data = driver.find_element_by_tag_name('tbody').find_elements_by_tag_name("tr")

    format_of_data = data[0].text.split()  # Because first line contains headings

    data = data[1:]  # removing the headings

    e_data = {}

    count = len(data)

    count_format = len(format_of_data)

    for i in range(count):
        key = data[i].find_element_by_xpath('td[1]').text
        value = [int(data[i].find_element_by_xpath('td[' + str(j) + ']').text.replace(',', '')) for j in
                 range(2, count_format + 1)]
        e_data[key] = value

    print(e_data)
    print(format_of_data)

    return e_data, format_of_data


def output(format_of_data, st_data_dict, state_id):
    data_to_list = list(st_data_dict)
    state_name = data_to_list[state_id-1]
    state_data = st_data_dict[state_name]
    print(f"\n\n--------------------------- LATEST CORONA STAT OF {state_name.upper()} ------------------------")
    print(f"\n{format_of_data[1]} Cases: {state_data[0]}")
    print(f"\n{format_of_data[2]} Cases: {state_data[1]}")
    print(f"\n{format_of_data[3]} Cases: {state_data[2]}")
    print(f"\n{format_of_data[4]} Cases: {state_data[3]}")
    print("--------------------------------------------------------------------------------------------------------")

