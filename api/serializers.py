from rest_framework import serializers
from .models import User, MyUser, Product, Order, Manufacturer, Delivery, Review


# MyUser 모델은 User 객체의 OneToOneField 로 생성했다.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        # What model you're trying to serialize
        model = MyUser
        # fields = '__all__'
        fields = ('user', 'password', 'email', 'name', 'phone', 'gender',
                  'date_joined', 'address', 'date_of_birth', 'pro_num')
        '''
        사용자가 처음 가입시에 패스워드를 입력하지만, 사용자 프로필페이지에서는 패스워드 데이터를 보여주면 절대 안된다. 
        그렇기 때문에 ModelSerializer 에서 extra_kwargs 내부에 write_only 설정을 추가하여 해당 데이터를 직렬화시 포함시키지 않을 수 있다. 
        '''
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return MyUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.date_joined = validated_data.get('date_joined', instance.date_joined)
        instance.address = validated_data.get('address', instance.address)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        # instance.pro_num = validated_data.get('pro_num', instance.pro_num, required=False)
        instance.save()

        return instance


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


