from selenium.common import NoSuchCookieException
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def user_info(driver, link):

    user_id = link.split("/")[-1]

    try:
        name  = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x14qwyeo xw06pyt x579bpy xjkpybl x1xlr1w8 xzsf02u x1yc453h']"))).text
        print("name: ", name)
    except TimeoutException:
        name = 'N/A'
        print("name: ", name)

    about_button = link + "/about"
    driver.get(about_button)
    print(f"Processing URL: {driver.current_url}")
    print('About clicked')

    contact_and_basic_info = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Contact and basic info']")))
    contact_and_basic_info.click()
    print('contact_and_basic_info clicked')


    # Wait for the 'Contact info' section to load
    try:
        contact_info_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//h2[span[text()='Contact info']]")
            )
        )
        print("Contact info section located.")

        # Locate the 'No contact info to show' element relative to the 'Contact info' element
        contact_info_element_detail = contact_info_element.find_element(
            By.XPATH,
            ".//following::span"
        ).text
        contact_number = contact_info_element_detail
        print(f"Element text: {contact_number}")

    except TimeoutException:
        contact_number = "N/A"
        print("contact number: ", contact_number)


    # Wait for the 'Gender' section to load
    try:
        # Locate the "Gender" text element
        gender_label = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//h2[span[text()='Basic info']]")
            )
        )

        # Locate the sibling or related element containing the gender value (e.g., "Female")
        gender_value = gender_label.find_element(
            By.XPATH,
            ".//following::span"
        ).text

        print(f"Gender: {gender_value}")

    except TimeoutException:
        gender_value = "N/A"
        print("gender: ",gender_value)


    # Wait for the 'Relationship' element to load
    try:
        family_and_relationship = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[text()='Family and relationships']")
        )
        )
        family_and_relationship.click()

        # Locate the "Relationship" heading element
        relationship_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//h2[span[text()='Relationship']]")
            )
        )

        # Locate the text element that appears after "Relationship"
        relationship_info = relationship_element.find_element(
            By.XPATH,
            ".//following::span"
        ).text

        # Print the text
        print(f"Relationship Info: {relationship_info}")  # Output: No relationship info to show

    except TimeoutException:
        relationship_info = 'N/A'
        print('relationship info: ', relationship_info)

    # click work and eduction tab
    work_and_education = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[text()='Work and education']")
        )
        )
    work_and_education.click()
    # work
    try:
        # Locate the "Work" section
        work_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//h2[span[text()='Work']]/ancestor::div[@class= 'x1gan7if']"
                 )
            )
        )
        # Find all job entries within the "Work" section
        job_entries = work_section.find_elements(By.XPATH, ".//div[@class='x13faqbe x78zum5 xdt5ytf']")

        # Extract job details
        work = []
        for job in job_entries:
            # Extract job title and company
            try:
                job_title = job.find_element(By.XPATH,
                                             ".//span[contains(text(), 'at')]").text

                print(f"Job Title: {job_title}")
                work.append(job_title)
            except NoSuchElementException:
                work = work_section.find_element(By.XPATH, './/following::span').text
                print('work: ', work)
        print("work_list: ", work)
    except TimeoutException:
        work = "N/A"
        print('work: ', work)

    # college
    try:
        # Locate the "College" section
        college_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//h2[span[text()='College']]/ancestor::div[@class= 'x1gan7if']"
                 )
            )
        )
        college_list = []
        colleges = college_section.find_elements(By.XPATH, ".//span[contains(text(), 'at')]")
        for col in colleges:
            college_list.append(col.text)

        print('College: ', college_list)
        if len(college_list) == 0:
            college_list = 'N/A'
    except TimeoutException:
        college_list = 'N/A'
        print('college: ', college_list)

    # High School
    try:
        # Locate the "College" section
        high_school_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//h2[span[text()='High school']]/ancestor::div[3]"
                 )
            )
        )
        high_school_list = []
        high_schools = high_school_section.find_elements(By.XPATH, ".//span[contains(text(), 'Went to')]")
        for high in high_schools:
            high_school_list.append(high.text)
        print('High School: ', high_school_list)
        if len(high_school_list) == 0:
            high_school_list = 'N/A'
    except TimeoutException:
        high_school_list = 'N/A'
        print('High school: ', high_school_list)

    # hometown
    try:
        #click places lived
        places_and_lived = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Places lived']"))

        )
        places_and_lived.click()

        #located place lived
        places_lived = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='xyamay9 xqmdsaz x1gan7if x1swvt13']"
                 )
            )
        )
        places_list = []
        places_element = places_lived.find_elements(By.XPATH, ".//span[text()='Hometown']/ancestor::div[3]")
        for hometown in places_element:
            places_list.append(hometown.text.replace("Hometown", "").strip())
        print("hometown: ", places_list)
        if len(places_list) == 0:
            places_list = "N/A"
    except TimeoutException:
        places_list = "N/A"
        print("hometown: ", places_list)

    contact_dict = {
        "User ID": user_id,
        "Name": name,
        "Contact info": contact_number,
        "Gender": gender_value,
        "Relationship info": relationship_info,
        "Work": work,
        "College": college_list,
        "High School": high_school_list,
        "Hometown": places_list,
    }

    return contact_dict


