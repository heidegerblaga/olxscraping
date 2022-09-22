from sqlalchemy import create_engine,Integer,String,Column,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///crawler.db',echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Crawler(Base):

    __tablename__="olxestate"

    id = Column(Integer, primary_key=True)
    property = Column(String)
    price = Column(Integer)
    metrprice = Column(Integer)
    market = Column(String)
    area = Column(Integer)
    plotarea = Column(Integer)
    building = Column(String)
    offerid = Column(Integer)

    def __repr__(self):
        return f'''<Crawler(property={self.property},price={self.price},metrprice={self.metrprice}, 
               market={self.market},area={self.area},plotarea={self.plotarea},building={self.building})>'''


if __name__ == '__main__':
    Base.metadata.create_all(engine)

