from time import sleep

from selene import have, browser


browser.open('http://www.google.com')
browser.element('.gLFyf').type('yashaka selene').press_enter()
browser.all('.g')[0].element('a').click()
browser.all('[href="/yashaka/selene"]').should(have.size(3))

