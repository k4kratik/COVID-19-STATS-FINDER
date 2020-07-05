def get_india_stat(driver):

    driver.get("https://www.mohfw.gov.in/")

    ind_active = int(driver.find_elements_by_class_name("bg-blue")[0].text.split()[0])

    ind_discharged = int(driver.find_elements_by_class_name("bg-green")[0].text.split()[0])

    ind_deaths = int(driver.find_elements_by_class_name("bg-red")[0].text.split()[0])

    # Output Section -
    print("")
    print("COVID-19 - CURRENT STATUS IN INDIA ")
    print("Active Cases:    \t", ind_active)
    print("Discharged Cases:\t", ind_discharged)
    print("Death Cases:     \t", ind_deaths, "\n")
