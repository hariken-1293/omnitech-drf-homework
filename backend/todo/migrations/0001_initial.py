from django.db import migrations, models


def set_default_user(apps, schema_editor):
    User = apps.get_model("auth", "User")
    TodoItem = apps.get_model("todo", "TodoItem")
    default_user = User.objects.first()  # デフォルトユーザーとして最初のユーザーを選択
    if default_user:  # デフォルトユーザーが存在する場合のみ更新
        TodoItem.objects.filter(user__isnull=True).update(user=default_user)


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TodoItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("completed", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        to="auth.User", on_delete=models.CASCADE, default=1
                    ),
                ),  # デフォルトIDを設定
            ],
        ),
        migrations.RunPython(
            set_default_user
        ),  # マイグレーション後にデフォルトユーザーを設定
    ]
