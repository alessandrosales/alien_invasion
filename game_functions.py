import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)

def fire_bullet(ia_settings, screen, ship, bullets):
	if len(bullets) < ia_settings.bullets_allowed:
		new_bullet = Bullet(ia_settings, screen, ship)
		bullets.add(new_bullet)

def update_bullets(bullets):
	bullets.update()

	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	print(len(bullets))

def update_screen(ia_settings, screen, ship, bullets):
	screen.fill(ia_settings.bg_color)

	for bullet in bullets.sprites():
		bullet.draw_bullet();

	ship.blitme()

	pygame.display.flip()
