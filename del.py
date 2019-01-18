import vk_api, time

ac_token = '' # access_token

owner_id = 0 # owner_id

vk_session = vk_api.VkApi(token = ac_token)
vk = vk_session.get_api()

r = vk.wall.get(count = 1, offset = 1)
print("Удаление {} записей запущено!".format(int(r['items'][0]['id'])))

i = int(r['items'][0]['id'])


while i > 0:
	post = vk.wall.getById(posts = str(owner_id) + '_' + str(i))
	if(len(post)):
		vk.wall.delete(post_id = i)
	if i % 50 == 0:
		print("Удалена запись №{}".format(i))
	i -= 1
	time.sleep(0.001)

print("Удаление завершено!")
