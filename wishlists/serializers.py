from rest_framework.serializers import ModelSerializer
from rooms.serializers import RoomListSerializer
from .models import Wishlists


class WishlistSerializer(ModelSerializer):
    rooms = RoomListSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Wishlists
        fields = (
            "pk",
            "name",
            "rooms",
        )
