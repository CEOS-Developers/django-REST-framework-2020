from rest_framework import serializers
from .models import User, MyUser, Product, Order, Manufacturer, Delivery, Review


# MyUser 모델은 User 객체의 OneToOneField 로 생성했다.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'password', 'email', 'username',
                  'is_staff', 'is_active', 'is_superuser', 'last_login')
        '''
        사용자가 처음 가입시에 패스워드를 입력하지만, 사용자 프로필페이지에서는 패스워드 데이터를 보여주면 안 된다. 
        그렇기 때문에 ModelSerializer 에서 extra_kwargs 내부에 write_only 설정을 추가하여 해당 데이터를 직렬화시 포함시키지 않을 수 있다. 
        '''
        extra_kwargs = {
            "password": {"write_only": True},
        }


# 회원가입 시리얼라이저
class MyUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        # What model you're trying to serialize
        model = MyUser
        # fields = '__all__'
        fields = ('user', 'phone', 'gender', 'date_joined', 'address', 'date_of_birth', 'product')
        extra_kwargs = {
                        "date_joined": {"read_only": True},
                        "product": {"read_only": True}
                        }

    def create(self, validated_data):
        myuser = MyUser.objects.create_user(**validated_data)
        return myuser

    def update(self, instance, validated_data):
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.date_joined = validated_data.get('date_joined', instance.date_joined)
        instance.address = validated_data.get('address', instance.address)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        # instance.product = validated_data.get('product', instance.product, required=False)
        instance.save()

        return instance


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('pro_num', 'pro_name', 'inventory', 'price', 'manufacturer', 'supply_date', 'supply_vol')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('myuser', 'product', 'quantity', 'destination', 'date_ordered', 'message')
        extra_kwargs = {"date_ordered": {"read_only": True}}


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('manu_num', 'manu_name', 'phone', 'address', 'supervisor')


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ('delivery_num', 'order', 'date_delivered', 'transport', 'state')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('review_num', 'myuser', 'order', 'title', 'image', 'content', 'pub_date')
        extra_kwargs = {"pub_date": {"read_only": True}}


