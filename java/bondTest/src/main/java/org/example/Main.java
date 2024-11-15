package org.example;
import com.opengamma.strata.basics.currency.Currency;
import com.opengamma.strata.basics.date.DayCounts;
import com.opengamma.strata.basics.date.HolidayCalendarIds;
import com.opengamma.strata.basics.date.BusinessDayAdjustment;
import com.opengamma.strata.market.curve.CurveName;
import com.opengamma.strata.basics.schedule.PeriodicSchedule;
import com.opengamma.strata.market.curve.RatesCurveGroup;
import com.opengamma.strata.pricer.bond.DiscountingFixedCouponBondProductPricer;
import com.opengamma.strata.pricer.rate.ImmutableRatesProvider;
import com.opengamma.strata.product.bond.ResolvedFixedCouponBond;
import com.opengamma.strata.product.bond.FixedCouponBond;
import com.opengamma.strata.product.bond.FixedCouponBondYieldConvention;
import com.opengamma.strata.product.LegalEntityId;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        // Set bond characteristics
        Currency currency = Currency.USD;
        LocalDate issueDate = LocalDate.of(2020, 1, 1);
        LocalDate maturityDate = LocalDate.of(2030, 1, 1);
        double couponRate = 0.05; // 5% coupon
        double notional = 1000000; // 1 million dollars
        LegalEntityId legalEntityId = LegalEntityId.parse("LE~1234");

        // Create a fixed coupon bond
        FixedCouponBond bond = FixedCouponBond.builder()
                .securityId(com.opengamma.strata.product.SecurityId.of("OG-Bond", "BOND1"))
                .currency(currency)
                .notional(notional)
                .dayCount(DayCounts.ACT_360)
                .fixedRate(couponRate)
                .accrualSchedule(PeriodicSchedule.builder()
                        .startDate(issueDate)
                        .endDate(maturityDate)
                        .frequency(com.opengamma.strata.basics.schedule.Frequency.P6M)
                        .businessDayAdjustment(BusinessDayAdjustment.of(
                                com.opengamma.strata.basics.date.BusinessDayConventions.MODIFIED_FOLLOWING,
                                HolidayCalendarIds.SAT_SUN))
                        .build())
                .settlementDateOffset(com.opengamma.strata.basics.date.DaysAdjustment.ofBusinessDays(2, HolidayCalendarIds.SAT_SUN))
                .yieldConvention(FixedCouponBondYieldConvention.US_STREET)
                .legalEntityId(legalEntityId)
                .build();

        // Resolve the bond
        ResolvedFixedCouponBond resolvedBond = bond.resolve(com.opengamma.strata.basics.ReferenceData.standard());

        // Create a discounting bond pricer
        DiscountingFixedCouponBondProductPricer pricer = DiscountingFixedCouponBondProductPricer.DEFAULT;

        // Create a dummy rates provider (for simplicity, using today as the valuation date)
        LocalDate valuationDate = LocalDate.now();
        //ImmutableRatesProvider ratesProvider = ImmutableRatesProvider.builder(valuationDate).build();

        // Define the bond price (e.g., 102% of face value)
        double dirtyPrice = 102.0; // Dirty price in percentage of par value

        // Calculate the yield from the given clean price
        double calculatedYield = pricer.yieldFromDirtyPrice(resolvedBond, valuationDate, dirtyPrice);
        System.out.println("Calculated Yield: " + calculatedYield);

        // Calculate the modified duration from the calculated yield
        double modifiedDuration = pricer.modifiedDurationFromYield(resolvedBond, valuationDate, calculatedYield);
        System.out.println("Modified Duration: " + modifiedDuration);

        // Calculate the convexity from the yield
        double convexity = pricer.convexityFromYield(resolvedBond, valuationDate, calculatedYield);
        System.out.println("Convexity: " + convexity);
    }
}
