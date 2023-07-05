from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import json

options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--start-maximized")

# driver = webdriver.Chrome()
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

driver.get("https://app.leonardo.ai/auth/login")
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/div/div/div/div/button"))
)
element = driver.find_element(
    By.XPATH, "/html/body/div[1]/div/div/div/div/button").click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//*[@id='signInFormUsername']"))
)
driver.find_element(
    By.XPATH, "//*[@id='signInFormUsername']").send_keys("thuyetphamit@gmail.com")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//*[@id='signInFormPassword']"))
)
driver.find_element(
    By.XPATH, "//*[@id='signInFormPassword']").send_keys("Khanh2023@")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/form/input[3]"))
)

actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//*[@id='chakra-modal-:r15:']/button"))
)
driver.find_element(By.XPATH, "//*[@id='chakra-modal-:r15:']/button").click()


driver.get("https://app.leonardo.ai/community-feed")

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located(
        (By.CLASS_NAME, "chakra-card__body"))
)




def get_pop_up_data(Xpath):
    return_list = {}




    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, Xpath)))
    # close_button = driver.find_element(By.CLASS_NAME ,"chakra-modal__content-container")
    # close_button = driver.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/section/div[2]/div/div[1]/button")
    close_button = driver.find_element(By.XPATH, Xpath)


    # Name
    name_xpath = "/html/body/div[4]/div[3]/div/section/div[2]/div/div[1]/div[2]/div[1]/div[2]/div/h2"
    WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, name_xpath)))
    name_detail = driver.find_element(By.XPATH, name_xpath).text
    return_list['name']=name_detail

    # Main Prompt
    prompt_detail_xpath = "/html/body/div[4]/div[3]/div/section/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/p"
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, prompt_detail_xpath)))
    prompt_detail = driver.find_element(By.XPATH, prompt_detail_xpath).text
    return_list['prompt']=prompt_detail

    # Negative Prompt
    prompt_negative_detail_xpath = "/html/body/div[4]/div[3]/div/section/div[2]/div/div[1]/div[2]/div[3]/div/p"
    negative_detail_size = driver.find_elements(By.XPATH, prompt_negative_detail_xpath)
    if len(negative_detail_size) > 0:
        print(negative_detail_size[0].text)
        return_list['negative_prompt']=negative_detail_size[0].text
    
    # Image Prompt
    image_xpath = "/html/body/div[4]/div[3]/div/section/div[2]/div/div[1]/div[1]/div[2]/div/img"
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, image_xpath)))
    image_detail = driver.find_element(By.XPATH, image_xpath).get_attribute("src")
    return_list['img_source']=image_detail

    # Next Button
    # next_button_xpath = "/html/body/div[4]/div[3]/div/section/div[1]/div/button"
    # next_button = driver.find_element(By.XPATH, next_button_xpath)
    # next_button.click()
    close_button.click()
    # print(return_list)
    time.sleep(2)

    return return_list

    

def get_reccuring_data(file_object, end_count ):
    
    
    
    elements = driver.find_elements(By.CLASS_NAME, "chakra-card__body")
    print(len(elements))
    print("-"*100)
    elements = elements[end_count:(len(elements)-1)]
    for i, element in enumerate(elements):
        element.click()
        prompt_detail = get_pop_up_data("/html/body/div[4]/div[3]/div/section/div[2]/div/div[1]/button")
        
        json.dump(prompt_detail, file_object)
        if i < len(elements) - 1:
            file_object.write(",")  # Add comma for all elements except the last one
        if i == len(elements) - 1:

        

            ActionChains(driver)\
                .send_keys("End")\
                .perform()
                
            driver.implicitly_wait(10)

            end_count = i + 1
            get_reccuring_data(file_object, end_count)
            time.sleep(5)
    


if __name__ == "__main__":

    filename = "extract.json"
    with open(filename, 'a') as file_object:
        end_count = 0
        get_reccuring_data(file_object, end_count)
                
    driver.close()
