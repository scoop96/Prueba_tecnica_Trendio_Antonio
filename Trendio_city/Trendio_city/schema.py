import graphene
from graphene_django import DjangoObjectType
from world.models import Country, City

class CountryType(DjangoObjectType):
    total_population = graphene.Int()
    
    class Meta:
        model = Country
        fields = ("id", "country_name", "language", "cities")
    @classmethod
    def resolve_total_population(self, info):
        if self.cities.exists():
            return self.total_population()
        return 0

class CountryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        country_name = graphene.String(required=True)
        language = graphene.String(required=True)
        
    country = graphene.Field(CountryType)
    
    @classmethod
    def mutate(cls, root, info, language, id=None,country_name=None):
        
        country, created = Country.objects.update_or_create(country_name=country_name,language=language)
        return CountryMutation(country=country)










class CityType(DjangoObjectType):
    country_fk_id = graphene.Int()  # Define the country_fk_id field

    class Meta:
        model = City
        fields = ("id", "city_name", "population")

    def resolve_country_fk_id(self, info):
        return self.country_fk.id if self.country_fk else None        

class CityMutation(graphene.Mutation):
    class Arguments:
        city_name = graphene.String(required=True)
        country_fk = graphene.ID(required=True)
        population = graphene.Int(required=True)
        
    city = graphene.Field(CityType)
    
    @classmethod
    def mutate(cls, root, info, city_name, country_fk, population):
        country = Country.objects.get(pk=country_fk)
        city, created = City.objects.update_or_create(
            city_name=city_name,
            defaults={'country_fk': country, 'population': population}
        )
        return CityMutation(city=city)

class Query(graphene.ObjectType):
    all_countries = graphene.List(CountryType)
    city_by_city_name = graphene.List(CountryType,country_name = graphene.String(required=True))
    all_countries_with_cities = graphene.List(CountryType)
    
        
    def resolve_all_countries(root, info):
        return Country.objects.all()
    
    
    def resolve_city_by_city_name(root, info, city_name):
        try:
            return City.objects.get(city_name=city_name)
        except City.DoesNotExist:
            return None

    

    def resolve_all_countries_with_cities(self, info):
        return Country.objects.prefetch_related('cities')
    
    
    
    
class Mutation(graphene.ObjectType):
    update_country = CountryMutation.Field()
    create_city = CityMutation.Field()
    
schema = graphene.Schema(query=Query, mutation= Mutation ,auto_camelcase=False)