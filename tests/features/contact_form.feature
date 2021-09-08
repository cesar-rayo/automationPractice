@contact_form
Feature: Home Visualization
    As Customer,
    I want to be able to contact Automation practice


    Scenario Outline: Visit Contact page
        Given The Customer visits Home Page
        When The Customer goes to the Contact Page
        And The Customer selects the subject "<subject>"
        And The Customer fills the email "<email>"
        And The Customer fills the order "<order>"
        And The Customer uploads the file "<input_file>"
        And The Customer fills the message "<content>"
        Then The Customer submits the form
        And The Contact page responses "<result>"

    Examples:
        |      subject     |      email      | order | input_file |    content   |    result     |
        |     Webmaster    | some@domain.com |  111a | test_1.txt | some content |    suceess    |
        |     Webmaster    | some@domain.edu |       | test_1.txt | some content |    suceess    |
        |                  | some@domain.com |  111a | test_1.txt | some content | subject_error |
        |     Webmaster    |                 |  112a | test_2.pdf | some content |  email_error  |
        |     Webmaster    | some@domain.com |  113a | test_3.jpg |              | content_error |
        | Customer service | some@domain.co  |  214b | test_1.txt | some content |    suceess    |
        | Customer service | some@domain.es  |       | test_1.txt | some content |    suceess    |
        | Customer service |                 |  215b | test_2.pdf | some content |  email_error  |
        | Customer service | some@domain.com |  216b | test_3.jpg |              | content_error |
