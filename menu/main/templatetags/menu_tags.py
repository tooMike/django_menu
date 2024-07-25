from django import template

from main.models import MenuItem

register = template.Library()


@register.inclusion_tag('main/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    """Отображение меню."""
    request = context['request']
    current_path = request.path.strip('/')
    menu_items = MenuItem.objects.select_related('parent').filter(
        menu__name=menu_name
    )
    menu_dict = {}
    active_item = None
    path = []

    # Создаем словарь меню
    for menu_item in menu_items:
        # Находим выбранный элемент меню
        if menu_item.slug == current_path:
            active_item = menu_item
            # Собираем путь к активному элементу
            temp_item = menu_item
            while temp_item:
                path.append(temp_item)
                temp_item = temp_item.parent
        # Если у текущего пункта есть родительский пункт,
        # то добавляем это пункт в список подпунктов родительского пункта
        if menu_item.parent_id:
            menu_dict.setdefault(menu_item.parent_id, []).append(menu_item)
        # Если родительского пункта нет, то формируем список корневых пунктов
        else:
            menu_dict.setdefault('root', []).append(menu_item)

    # Обрабатываем элементы меню
    for menu_item in menu_items:
        # Добавляем каждому пункту меню список дочерних пунктов
        menu_item.children_list = menu_dict.get(menu_item.id, [])
        # Добавляем информацию, находится ли пункт меню в выбранной ветке
        # пунктов
        menu_item.is_in_active_path = menu_item in path
        # Добавляем информацию, является ли пункт выбранным
        menu_item.is_active = menu_item == active_item
        # Скрываем неактивные ветки
        if not menu_item.is_in_active_path and menu_item.children_list:
            menu_item.children_list = []

    root_items = menu_dict.get('root', [])
    return {'menu_items': root_items, 'active_item': active_item}
