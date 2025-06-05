import xml.etree.ElementTree as ET

def get_page_source(driver):
    return driver.page_source

def extract_ui_elements(xml_source):
    root = ET.fromstring(xml_source)
    ui_elements = []
    for element in root.iter():
        text = element.attrib.get("text", "")
        resource_id = element.attrib.get("resource-id", "")
        content_desc = element.attrib.get("content-desc", "")
        class_name = element.attrib.get("class", "")
        if text or resource_id or content_desc:
            ui_elements.append({
                "text": text,
                "resource-id": resource_id,
                "content-desc": content_desc,
                "class": class_name
            })
    return ui_elements[:5]
